@echo off
chcp 65001 >nul 2>&1
echo ============================================
echo   Revue de Memoires - Demarrage
echo ============================================
echo.

if not exist "venv\Scripts\python.exe" (
    echo ERREUR : L'environnement virtuel n'existe pas.
    echo Lancez d'abord : setup.bat
    pause
    exit /b 1
)

echo Serveur en cours de demarrage (hot reload actif)...
echo Ouvrez http://localhost:5000 dans votre navigateur.
echo Appuyez sur Ctrl+C pour arreter.
echo.

venv\Scripts\python.exe -m uvicorn app:asgi_app --host 127.0.0.1 --port 5000 --reload --reload-include "*.html" --reload-include "*.css" --reload-include "*.js" --reload-include "*.env"
pause
