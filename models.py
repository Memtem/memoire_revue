import json
import os
import sqlite3

from config import DB_PATH, DATA_DIR


def get_db():
    os.makedirs(DATA_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_db()
    schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
    with open(schema_path, 'r', encoding='utf-8') as f:
        conn.executescript(f.read())
    conn.close()


# --- Students ---

def create_student(nom, prenom, email='', promotion=''):
    conn = get_db()
    cur = conn.execute(
        "INSERT INTO students (nom, prenom, email, promotion) VALUES (?, ?, ?, ?)",
        (nom, prenom, email, promotion)
    )
    conn.commit()
    student_id = cur.lastrowid
    conn.close()
    return student_id


def get_all_students():
    conn = get_db()
    rows = conn.execute(
        "SELECT * FROM students ORDER BY nom, prenom"
    ).fetchall()
    conn.close()
    return rows


def find_student_by_name(nom, prenom):
    conn = get_db()
    row = conn.execute(
        "SELECT * FROM students WHERE LOWER(TRIM(nom)) = LOWER(TRIM(?)) AND LOWER(TRIM(prenom)) = LOWER(TRIM(?))",
        (nom, prenom)
    ).fetchone()
    conn.close()
    return row


def get_student(student_id):
    conn = get_db()
    row = conn.execute(
        "SELECT * FROM students WHERE id = ?", (student_id,)
    ).fetchone()
    conn.close()
    return row


def update_student(student_id, nom, prenom, email='', promotion=''):
    conn = get_db()
    conn.execute(
        "UPDATE students SET nom=?, prenom=?, email=?, promotion=? WHERE id=?",
        (nom, prenom, email, promotion, student_id)
    )
    conn.commit()
    conn.close()


def delete_student(student_id):
    conn = get_db()
    conn.execute("DELETE FROM reviews WHERE student_id = ?", (student_id,))
    conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()


# --- Reviews ---

def create_review(student_id, etape, filename, document_text,
                  criteria_results, points_forts, ameliorations,
                  appreciation, email_body):
    conn = get_db()
    cur = conn.execute(
        """INSERT INTO reviews
        (student_id, etape, filename, document_text, criteria_results,
         points_forts, ameliorations, appreciation, email_body)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (student_id, etape, filename, document_text,
         json.dumps(criteria_results, ensure_ascii=False),
         points_forts, ameliorations, appreciation, email_body)
    )
    conn.commit()
    review_id = cur.lastrowid
    conn.close()
    return review_id


def delete_review(review_id):
    conn = get_db()
    conn.execute("DELETE FROM reviews WHERE id = ?", (review_id,))
    conn.commit()
    conn.close()


def get_review(review_id):
    conn = get_db()
    row = conn.execute(
        "SELECT * FROM reviews WHERE id = ?", (review_id,)
    ).fetchone()
    conn.close()
    if row:
        row = dict(row)
        row['criteria_results'] = json.loads(row['criteria_results']) if row['criteria_results'] else []
    return row


def get_reviews_for_student(student_id):
    conn = get_db()
    rows = conn.execute(
        "SELECT * FROM reviews WHERE student_id = ? ORDER BY created_at DESC",
        (student_id,)
    ).fetchall()
    conn.close()
    results = []
    for row in rows:
        r = dict(row)
        r['criteria_results'] = json.loads(r['criteria_results']) if r['criteria_results'] else []
        results.append(r)
    return results


def get_recent_reviews(limit=20):
    conn = get_db()
    rows = conn.execute(
        """SELECT r.*, s.nom, s.prenom
        FROM reviews r JOIN students s ON r.student_id = s.id
        ORDER BY r.created_at DESC LIMIT ?""",
        (limit,)
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]


def get_previous_reviews(student_id, etape):
    """Get previous reviews for continuity feedback."""
    conn = get_db()
    rows = conn.execute(
        """SELECT etape, criteria_results, points_forts, ameliorations, appreciation, created_at
        FROM reviews WHERE student_id = ? ORDER BY created_at ASC""",
        (student_id,)
    ).fetchall()
    conn.close()
    results = []
    for row in rows:
        r = dict(row)
        r['criteria_results'] = json.loads(r['criteria_results']) if r['criteria_results'] else []
        results.append(r)
    return results


def get_stats():
    conn = get_db()
    total_students = conn.execute("SELECT COUNT(*) FROM students").fetchone()[0]
    total_reviews = conn.execute("SELECT COUNT(*) FROM reviews").fetchone()[0]
    reviews_by_etape = conn.execute(
        "SELECT etape, COUNT(*) as cnt FROM reviews GROUP BY etape"
    ).fetchall()
    conn.close()
    return {
        'total_students': total_students,
        'total_reviews': total_reviews,
        'reviews_by_etape': {row['etape']: row['cnt'] for row in reviews_by_etape},
    }
