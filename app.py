import os
import traceback

from flask import (Flask, flash, redirect, render_template, request,
                   url_for)
from werkzeug.utils import secure_filename

from config import ETAPE_LABELS, ETAPES, MAX_CONTENT_LENGTH, SESSIONS, UPLOAD_DIR
from document_parser import allowed_file, extract_text
from export import format_email
from models import (create_review, create_student, delete_review,
                    delete_student, get_all_students, get_previous_reviews,
                    get_recent_reviews, get_review, get_reviews_for_student,
                    get_stats, get_student, init_db, update_student)
from prompts import get_criteres_by_categorie
from review_engine import analyze_document

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.before_request
def ensure_db():
    init_db()


# --- Dashboard ---

@app.route('/')
def index():
    stats = get_stats()
    recent = get_recent_reviews(10)
    return render_template('index.html', stats=stats, recent=recent,
                           etape_labels=ETAPE_LABELS)


# --- Reviews ---

@app.route('/review', methods=['GET', 'POST'])
def review():
    students = get_all_students()

    if request.method == 'POST':
        student_id = request.form.get('student_id')
        etape = request.form.get('etape')
        pasted_text = request.form.get('pasted_text', '').strip()
        file = request.files.get('document')

        if not student_id or not etape:
            flash("Veuillez sélectionner un étudiant et une étape.", "danger")
            return redirect(url_for('review'))

        # Extract document text
        document_text = ''
        filename = ''

        if file and file.filename and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_DIR, filename)
            file.save(filepath)
            try:
                document_text = extract_text(filepath)
            except Exception as e:
                flash(f"Erreur lors de l'extraction du fichier : {e}", "danger")
                return redirect(url_for('review'))
            finally:
                if os.path.exists(filepath):
                    os.remove(filepath)
        elif pasted_text:
            document_text = pasted_text
            filename = 'texte_collé'
        else:
            flash("Veuillez uploader un fichier (.docx/.pdf) ou coller du texte.", "danger")
            return redirect(url_for('review'))

        if len(document_text.strip()) < 50:
            flash("Le texte extrait est trop court (moins de 50 caractères). Vérifiez votre document.", "warning")
            return redirect(url_for('review'))

        # Get previous reviews for continuity
        previous = get_previous_reviews(int(student_id), etape)

        # Analyze with Claude
        try:
            result = analyze_document(etape, document_text, previous)
        except ValueError as e:
            flash(str(e), "danger")
            return redirect(url_for('review'))
        except Exception as e:
            flash(f"Erreur lors de l'analyse : {e}", "danger")
            traceback.print_exc()
            return redirect(url_for('review'))

        # Format email
        student = get_student(int(student_id))
        email_body = format_email(dict(student), etape, result)

        # Save review
        review_id = create_review(
            student_id=int(student_id),
            etape=etape,
            filename=filename,
            document_text=document_text[:5000],  # Store first 5000 chars only
            criteria_results=result['criteria_results'],
            points_forts=result['points_forts'],
            ameliorations=result['ameliorations'],
            appreciation=result['appreciation'],
            email_body=email_body,
        )

        return redirect(url_for('result', review_id=review_id))

    return render_template('review.html', students=students, etapes=ETAPES)


@app.route('/result/<int:review_id>')
def result(review_id):
    rev = get_review(review_id)
    if not rev:
        flash("Revue introuvable.", "danger")
        return redirect(url_for('index'))
    student = get_student(rev['student_id'])
    return render_template('result.html', review=rev, student=student,
                           etape_labels=ETAPE_LABELS)


@app.route('/reviews/<int:review_id>/delete', methods=['POST'])
def remove_review(review_id):
    rev = get_review(review_id)
    if not rev:
        flash("Revue introuvable.", "danger")
        return redirect(url_for('index'))
    student_id = rev['student_id']
    delete_review(review_id)
    flash("Revue supprimée.", "success")
    return redirect(url_for('student_detail', student_id=student_id))


# --- Students ---

@app.route('/students')
def students():
    current_session = request.args.get('session', '')
    all_students = get_all_students()
    if current_session:
        all_students = [s for s in all_students if s['promotion'] == current_session]
    return render_template('students.html', students=all_students,
                           sessions=SESSIONS, current_session=current_session)


@app.route('/students/add', methods=['POST'])
def add_student():
    nom = request.form.get('nom', '').strip()
    prenom = request.form.get('prenom', '').strip()
    email = request.form.get('email', '').strip()
    promotion = request.form.get('promotion', '').strip()
    if not nom or not prenom:
        flash("Le nom et le prénom sont obligatoires.", "danger")
        return redirect(url_for('students'))
    create_student(nom, prenom, email, promotion)
    flash(f"Étudiant {prenom} {nom} ajouté.", "success")
    return redirect(url_for('students'))


@app.route('/students/<int:student_id>/edit', methods=['POST'])
def edit_student(student_id):
    nom = request.form.get('nom', '').strip()
    prenom = request.form.get('prenom', '').strip()
    email = request.form.get('email', '').strip()
    promotion = request.form.get('promotion', '').strip()
    if not nom or not prenom:
        flash("Le nom et le prénom sont obligatoires.", "danger")
        return redirect(url_for('student_detail', student_id=student_id))
    update_student(student_id, nom, prenom, email, promotion)
    flash("Informations mises à jour.", "success")
    return redirect(url_for('student_detail', student_id=student_id))


@app.route('/students/<int:student_id>/delete', methods=['POST'])
def remove_student(student_id):
    delete_student(student_id)
    flash("Étudiant supprimé.", "success")
    return redirect(url_for('students'))


@app.route('/students/<int:student_id>')
def student_detail(student_id):
    student = get_student(student_id)
    if not student:
        flash("Étudiant introuvable.", "danger")
        return redirect(url_for('students'))
    reviews = get_reviews_for_student(student_id)
    return render_template('student.html', student=student, reviews=reviews,
                           etape_labels=ETAPE_LABELS, etapes=ETAPES, sessions=SESSIONS)


# ASGI wrapper pour uvicorn
from a2wsgi import WSGIMiddleware
asgi_app = WSGIMiddleware(app)

if __name__ == '__main__':
    init_db()
    import uvicorn
    uvicorn.run('app:asgi_app', host='127.0.0.1', port=5000, reload=True)
