@echo off
chcp 65001 >nul 2>&1
echo ============================================
echo   Installation - Revue de Memoires
echo ============================================
echo.

REM Trouver Python : essayer py, python, python3
set PYTHON_CMD=
where py >nul 2>&1
if not errorlevel 1 (
    set PYTHON_CMD=py
    goto :found
)
where python >nul 2>&1
if not errorlevel 1 (
    set PYTHON_CMD=python
    goto :found
)
where python3 >nul 2>&1
if not errorlevel 1 (
    set PYTHON_CMD=python3
    goto :found
)

echo ERREUR : Python n'est pas installe ou pas dans le PATH.
echo Telechargez Python depuis https://www.python.org/downloads/
echo IMPORTANT : Cochez "Add Python to PATH" lors de l'installation.
pause
exit /b 1

:found
echo Python trouve : %PYTHON_CMD%
%PYTHON_CMD% --version
echo.

echo [1/3] Creation de l'environnement virtuel...
if exist "venv\Scripts\python.exe" (
    echo    Environnement virtuel deja present.
) else (
    if exist "venv" rmdir /s /q venv
    %PYTHON_CMD% -m venv venv
    if not exist "venv\Scripts\python.exe" (
        echo ERREUR : Impossible de creer l'environnement virtuel.
        echo Essayez : %PYTHON_CMD% -m pip install virtualenv
        pause
        exit /b 1
    )
    echo    Environnement virtuel cree.
)

echo [2/3] Installation des dependances...
venv\Scripts\python.exe -m pip install --upgrade pip
venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 (
    echo ERREUR : L'installation des dependances a echoue.
    pause
    exit /b 1
)

echo [3/3] Verification de la configuration...
if not exist ".env" (
    echo ATTENTION : Le fichier .env n'existe pas.
    echo Creez un fichier .env avec votre cle API Gemini.
)

echo.
echo ============================================
echo   Installation terminee !
echo.
echo   IMPORTANT : Editez le fichier .env pour
echo   y mettre votre cle API Google Gemini.
echo   (gratuite sur https://aistudio.google.com/apikey)
echo.
echo   Lancez ensuite : run.bat
echo ============================================
pause
