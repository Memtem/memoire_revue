# Revue de Memoires

Application web d'aide a la correction de memoires professionnels (Bac+3 a Bac+5) utilisant l'IA generative Google Gemini.

L'outil permet aux formateurs d'evaluer les travaux des apprenants a chaque etape de redaction, selon une grille de criteres pedagogiques structuree, et de generer automatiquement un retour detaille pret a etre envoye par email.

## Fonctionnalites

- **Gestion des etudiants** : ajout, modification, suppression, filtrage par promotion
- **Analyse automatisee par IA** : evaluation du document selon une grille de criteres adaptee a l'etape du memoire (sujet, problematique, plan, plan detaille, V1, version finale)
- **Grille de 48 criteres** repartis en 9 categories : problematique, plan, introduction, partie theorique, partie pratique, preconisations, conclusion, forme et redaction
- **Verification RNCP AMOA** : a l'etape sujet, verification que l'apprenant mentionne au moins 3 competences du referentiel RNCP35269 (46 competences)
- **Suivi de progression** : prise en compte des retours precedents pour mesurer l'evolution de l'apprenant
- **Generation d'email** : formatage automatique du retour en email structure, pret a copier
- **Import de documents** : support des formats `.docx` et `.pdf`, ou saisie directe du texte
- **Tableau de bord** : statistiques globales et historique des revues recentes

## Etapes du memoire

| Etape | Criteres evalues |
|---|---|
| Sujet | 7 criteres : pertinence AMOA, perimetre, faisabilite, originalite, formulation du titre, pistes de problematiques, ancrage RNCP (min. 3 competences) |
| Problematique | 6 criteres |
| Plan | 12 criteres (problematique + plan) |
| Plan detaille | 19 criteres (+ introduction) |
| V1 | 48 criteres (evaluation bienveillante) |
| Version finale | 48 criteres (evaluation exigeante) |

### Distinction sujet / problematique

- **Sujet** : futur titre du memoire, theme general et englobant. L'apprenant propose un perimetre large de reflexion.
- **Problematique** : question de recherche precise et delimitee, formulee a l'etape suivante.

## Stack technique

- **Backend** : Python 3.12+, Flask, Uvicorn (ASGI via a2wsgi)
- **IA** : Google Gemini (gemini-2.5-flash)
- **Base de donnees** : SQLite
- **Frontend** : Bootstrap 5, Bootstrap Icons, Jinja2
- **Parsing documents** : python-docx, pypdf

## Prerequis

- Python 3.12 ou superieur
- Une cle API Google Gemini gratuite ([obtenir ici](https://aistudio.google.com/apikey))

## Installation

### Windows (recommande)

1. Cloner le depot :
   ```bash
   git clone https://github.com/Memtem/memoire_revue.git
   cd memoire_revue
   ```

2. Lancer le script d'installation :
   ```bash
   setup.bat
   ```

3. Creer un fichier `.env` a la racine du projet :
   ```
   GEMINI_API_KEY=votre-cle-api-gemini
   GEMINI_MODEL=gemini-2.5-flash
   MAX_TOKENS=8192
   ```

4. Demarrer le serveur :
   ```bash
   run.bat
   ```

5. Ouvrir [http://localhost:5000](http://localhost:5000) dans le navigateur.

### Manuel (Linux / macOS)

```bash
git clone https://github.com/Memtem/memoire_revue.git
cd memoire_revue
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Creer le fichier `.env` comme indique ci-dessus, puis :

```bash
uvicorn app:asgi_app --host 127.0.0.1 --port 5000 --reload
```

## Structure du projet

```
memoire-review/
├── app.py               # Application Flask (routes et logique web)
├── config.py            # Configuration (chemins, modele IA, etapes)
├── models.py            # Couche base de donnees (SQLite)
├── schema.sql           # Schema de la base de donnees
├── document_parser.py   # Extraction de texte (.docx, .pdf)
├── review_engine.py     # Moteur d'analyse via Google Gemini
├── prompts.py           # Criteres d'evaluation et prompts IA
├── export.py            # Generation de l'email de retour
├── requirements.txt     # Dependances Python
├── setup.bat            # Script d'installation Windows
├── run.bat              # Script de lancement Windows
├── .env                 # Variables d'environnement (non versionne)
├── templates/           # Templates HTML (Jinja2)
│   ├── base.html
│   ├── index.html
│   ├── review.html
│   ├── result.html
│   ├── students.html
│   └── student.html
└── static/
    ├── css/style.css
    └── js/app.js
```

## Configuration

Les variables d'environnement sont definies dans le fichier `.env` :

| Variable | Description | Valeur par defaut |
|---|---|---|
| `GEMINI_API_KEY` | Cle API Google Gemini (obligatoire) | - |
| `GEMINI_MODEL` | Modele Gemini a utiliser | `gemini-2.5-flash` |
| `MAX_TOKENS` | Nombre max de tokens en reponse | `8192` |

## Utilisation

1. **Ajouter des etudiants** via l'onglet "Etudiants"
2. **Lancer une revue** via "Nouvelle revue" : selectionner l'etudiant, l'etape, puis importer le document ou coller le texte
3. **Consulter le resultat** : criteres evalues, points forts, ameliorations, appreciation generale
4. **Copier l'email** genere automatiquement pour l'envoyer a l'apprenant
5. **Suivre la progression** via la fiche etudiant qui centralise l'historique des revues

## Licence

Usage interne formateur.
