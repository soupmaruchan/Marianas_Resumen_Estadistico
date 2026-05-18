# Pretty Cute Closet

App de escritorio hecha con Python + Tkinter.

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

## Proyecto realizado por:
- Mariana Fabiola Cisneros García
- Jennifer Atziri Mariscal Magaña
- Elena Yaretzi Ochoa Jarrillo
- Esthela Naomi Oroz Leal
