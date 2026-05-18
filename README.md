# Pretty Cute Closet

App de escritorio kawaii hecha con Python + Tkinter.

## Que incluye

- Inicio con boton START grande.
- Menu principal con Closet, Diario, Gato y Galeria.
- Closet por categorias con flechas que aparecen segun el icono elegido.
- Pantalla de avatar listo para guardar dentro de la app o descargar.
- Galeria de avatares guardados; al tocar una foto se copia a Descargas.
- Diario con animacion de hoja y carga de imagenes desde tu computadora.
- Gato con piezas mas grandes y navegacion igual al resto de la app.

## Instalar para correr en VS Code

1. Instala Python 3.11 o superior desde python.org.
2. En el instalador marca `Add python.exe to PATH`.
3. En VS Code instala la extension `Python` de Microsoft.
4. Abre esta carpeta y ejecuta:

```bash
python -m pip install pillow
```

Opcional para que suene el `click.mp3` real:

```bash
python -m pip install pygame
```

Si no instalas `pygame`, la app usa un sonido simple de Windows como fallback.

## Ejecutar

```bash
python -B main.py
```

Tambien puedes usar el boton Play de VS Code. El codigo ya activa
`sys.dont_write_bytecode = True`, asi que no deberia seguir creando nuevos
`__pycache__` al correr desde `main.py`.

## Carpetas que se crean solas

- `datos/galeria`: avatares guardados dentro de la app.
- `datos/diario_imagenes`: imagenes subidas al diario.
- `Downloads/PrettyCuteCloset`: copias descargadas a tu computadora.

Cuando se usa el `.exe`, los datos se guardan en
`Documents/PrettyCuteCloset/datos` para que no se pierdan al cerrar la app.

No necesitas crear esas carpetas a mano.

## Crear una app descargable

Instala PyInstaller:

```bash
python -m pip install pyinstaller
```

Luego genera el ejecutable con el icono de libreta:

```bash
pyinstaller --onefile --windowed --clean --name "Pretty Cute Closet" --icon "assets/icono_app.ico" --add-data "pantashas;pantashas" --add-data "assets;assets" --add-data "datos;datos" main.py
```

El `.exe` queda en `dist/Pretty Cute Closet.exe`. Tambien puedes abrir
`crear_app.bat` para que instale lo necesario y genere el ejecutable solo.
Al compartir solo el `.exe`, el codigo queda empaquetado dentro de la app y
no se entrega como archivos `.py` sueltos.

## Compartirla con otras personas

Tienes dos formas bonitas:

1. Compartir el proyecto completo:
   - Sube la carpeta a GitHub desde VS Code.
   - Quien la descargue instala Python y corre `python -B main.py`.
   - Es la mejor opcion para profes o personas que quieran ver el codigo.

2. Compartir solo la app:
   - Genera el ejecutable con PyInstaller.
   - Comprime la carpeta `dist` en `.zip`.
   - Sube ese `.zip` a Google Drive, GitHub Releases o un link de descarga.
   - Quien lo descargue abre el `.exe` sin tocar el codigo.

## Subirla a GitHub como descargable

Para que cualquiera descargue la app sin ver el codigo, crea un repositorio
publico solo para descargas y sube ahi el `.zip` de `dist` como Release.
Guarda el proyecto con codigo en un repositorio privado o en tu computadora.

Pasos:

1. Abre `crear_app.bat` y espera a que cree `dist/Pretty Cute Closet.exe`.
2. Da clic derecho sobre la carpeta `dist` y comprimela en `.zip`.
3. En GitHub crea un repositorio publico, por ejemplo `pretty-cute-closet`.
4. En el repositorio entra a `Releases` > `Create a new release`.
5. Escribe un tag como `v1.0.0`, titulo `Pretty Cute Closet` y sube el `.zip`.
6. Publica la Release y comparte ese link.
