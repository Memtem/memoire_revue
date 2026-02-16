import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
UPLOAD_DIR = os.path.join(BASE_DIR, 'uploads')
DB_PATH = os.path.join(DATA_DIR, 'memoire.db')

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
GEMINI_MODEL = os.getenv('GEMINI_MODEL', 'gemini-2.5-flash')
MAX_TOKENS = int(os.getenv('MAX_TOKENS', '8192'))

ALLOWED_EXTENSIONS = {'docx', 'pdf'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB

ETAPES = [
    ('sujet', 'Sujet'),
    ('problematique', 'Problématique'),
    ('plan', 'Plan'),
    ('plan_detaille', 'Plan détaillé'),
    ('v1', 'V1'),
    ('version_finale', 'Version finale'),
]

ETAPE_LABELS = dict(ETAPES)

SESSIONS = [
    '2024-D09 ALT',
    '2025-D05 ALT',
    '2025-D15 CONT',
    '2025-D15 ALT',
]
