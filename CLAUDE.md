# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Flask web application for reviewing professional thesis documents (mémoires) using Google Gemini AI. French-language tool for educators evaluating student work across 6 stages, with 48 structured criteria and RNCP AMOA competency verification.

## Commands

```bash
# Install (Windows)
setup.bat

# Run (Windows) - starts on http://localhost:5000
run.bat

# Run (Linux/macOS)
source venv/bin/activate
uvicorn app:asgi_app --host 127.0.0.1 --port 5000 --reload

# Install dependencies manually
pip install -r requirements.txt
```

No test framework is configured.

## Architecture

```
app.py → Flask routes & request handling
  ├── config.py         → env vars, paths, ETAPES, SESSIONS constants
  ├── models.py         → SQLite CRUD (students, reviews) via schema.sql
  ├── document_parser.py → text extraction from .docx/.pdf
  ├── review_engine.py  → Gemini API calls with retry logic
  │    └── prompts.py   → 48 evaluation criteria + prompt construction
  └── export.py         → email formatting from review results
```

**Request flow**: Upload/paste document → `document_parser` extracts text → `review_engine` sends to Gemini with stage-appropriate prompt from `prompts.py` → response parsed as JSON → saved via `models.py` → email formatted via `export.py`.

## Key Design Decisions

- **Stage-specific evaluation**: `prompts.py` defines which criteria apply at each étape. The `sujet` stage has its own prompt (`_build_sujet_prompt`) with RNCP AMOA 46-competency verification. Other stages use `build_review_prompt` with progressively stricter criteria.
- **Continuity tracking**: `get_previous_reviews()` feeds past feedback into the AI prompt so it can acknowledge student progress or flag unaddressed issues.
- **ASGI via a2wsgi**: Flask app is wrapped with `WSGIMiddleware` for Uvicorn compatibility.
- **Document text truncated to 5000 chars** when stored in DB; prompts truncated at 200,000 chars before sending to Gemini.

## Configuration

Environment variables in `.env` (not versioned):
- `GEMINI_API_KEY` (required)
- `GEMINI_MODEL` (default: `gemini-2.5-flash`)
- `MAX_TOKENS` (default: `8192`)

## Conventions

- All UI text, prompts, criteria, and comments are in **French**.
- Email format: opens with "Salutations {prénom}", closes with "Bien à toi,", uses tutoiement.
- Gemini responses must be valid JSON matching the exact schema defined in `prompts.py`.
- Criteria statuses: `"OK"`, `"Partiel"`, `"Non"`.
