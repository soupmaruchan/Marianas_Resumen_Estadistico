setlocal
cd /d "%~dp0"

echo Instalando herramientas necesarias...
set "PY_CMD="
where py >nul 2>nul && set "PY_CMD=py"
if not defined PY_CMD (
    where python >nul 2>nul && set "PY_CMD=python"
)

if not defined PY_CMD (
    echo No se encontro Python. Instala Python y marca Add python.exe to PATH.
    pause
    exit /b 1
)

%PY_CMD% -m pip install pillow pyinstaller
if errorlevel 1 (
    echo No se pudieron instalar las herramientas.
    pause
    exit /b 1
)

echo Creando Pretty Cute Closet.exe...
%PY_CMD% -m PyInstaller --noconfirm --onefile --windowed --clean --name "Pretty Cute Closet" --icon "assets\icono_app.ico" --add-data "pantashas;pantashas" --add-data "assets;assets" --add-data "datos;datos" main.py

echo.
echo Listo. Tu app esta en: dist\Pretty Cute Closet.exe
echo Puedes compartir ese .exe o comprimir la carpeta dist en .zip.
pause
