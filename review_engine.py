import json
import re
import time

from google import genai
from google.genai import types

from config import GEMINI_API_KEY, GEMINI_MODEL, MAX_TOKENS
from prompts import SYSTEM_PROMPT, build_review_prompt

MAX_RETRIES = 3
RETRY_DELAY = 30  # seconds


def analyze_document(etape, document_text, previous_reviews=None):
    """Envoie le document à Gemini pour analyse et retourne le résultat structuré."""
    if not GEMINI_API_KEY or GEMINI_API_KEY == 'VOTRE-CLE-GEMINI-ICI':
        raise ValueError(
            "Clé API Gemini non configurée. "
            "Obtenez une clé gratuite sur https://aistudio.google.com/apikey "
            "puis modifiez le fichier .env."
        )

    client = genai.Client(api_key=GEMINI_API_KEY)

    user_prompt = build_review_prompt(etape, document_text, previous_reviews)

    # Truncate if too long
    if len(user_prompt) > 200000:
        user_prompt = user_prompt[:200000] + "\n\n[... document tronqué ...]"

    # Retry on rate limit errors
    for attempt in range(MAX_RETRIES):
        try:
            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    max_output_tokens=MAX_TOKENS,
                    temperature=0.3,
                ),
            )
            response_text = response.text
            return parse_response(response_text)
        except Exception as e:
            error_str = str(e)
            if '429' in error_str and attempt < MAX_RETRIES - 1:
                time.sleep(RETRY_DELAY)
                continue
            raise


def parse_response(response_text):
    """Parse la réponse JSON de Gemini."""
    json_match = re.search(r'\{[\s\S]*\}', response_text)
    if not json_match:
        raise ValueError("Impossible de trouver du JSON dans la réponse de Gemini.")

    try:
        data = json.loads(json_match.group())
    except json.JSONDecodeError as e:
        raise ValueError(f"Erreur de parsing JSON : {e}\nRéponse brute : {response_text[:500]}")

    return {
        'criteria_results': data.get('criteres', []),
        'points_forts': data.get('points_forts', ''),
        'ameliorations': data.get('ameliorations', ''),
        'appreciation': data.get('appreciation', ''),
    }
