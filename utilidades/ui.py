import itertools
import tkinter as tk

from utilidades.botonsitos import boton_en_canvas
from utilidades.cargador import Cargador
from utilidades.cursor_app import cursor_mano, cursor_normal


APP_W = 800
APP_H = 600
STICKERS = "pantashas/iconosystickers"
DISPLAY_FONT = "Trebuchet MS"
TITLE_FONT = "Cooper Black"
_TAG_COUNTER = itertools.count()


def crear_canvas(frame):
    canvas = tk.Canvas(frame, width=APP_W, height=APP_H, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    try:
        cursor_normal(canvas)
    except tk.TclError:
        pass
    return canvas


def fondo_suave(canvas, titulo=None):
    cursor_normal(canvas)
    colores = ["#ffc2df", "#ffd5e9", "#c8e5ff", "#b8dcff"]
    alto = APP_H // len(colores)
    for i, color in enumerate(colores):
        canvas.create_rectangle(0, i * alto, APP_W, (i + 1) * alto + 2,
                                fill=color, outline=color)

    for ruta, x, y, size in [
        (f"{STICKERS}/florrosasticker.png", 80, 110, (62, 62)),
        (f"{STICKERS}/cakesticker.png", 705, 88, (68, 68)),
        (f"{STICKERS}/floramrillasticker.png", 96, 510, (60, 60)),
        (f"{STICKERS}/stickerbomnito.png", 700, 512, (72, 72)),
    ]:
        img = Cargador.imagen(ruta, size)
        if img:
            canvas.create_image(x, y, image=img, anchor="center")

    if titulo:
        titulo_revista(canvas, 400, 48, titulo)


def fondo_imagen(canvas, ruta):
    cursor_normal(canvas)
    bg = Cargador.imagen(ruta, (APP_W, APP_H))
    if bg:
        canvas.create_image(0, 0, image=bg, anchor="nw")
    return bg


def texto_sombra(canvas, x, y, texto, font=None, fill="#ef4fa0",
                 shadow="#9dc8ef", anchor="center", tags=None):
    font = font or (DISPLAY_FONT, 13, "bold")
    canvas.create_text(x + 2, y + 2, text=texto, font=font, fill=shadow,
                       anchor=anchor, tags=tags)
    return canvas.create_text(x, y, text=texto, font=font, fill=fill,
                              anchor=anchor, tags=tags)


def titulo_revista(canvas, x, y, texto, size=28, tags=None):
    font = (TITLE_FONT, size, "bold")
    canvas.create_text(x + 3, y + 4, text=texto, font=font,
                       fill="#ffedf7", tags=tags)
    canvas.create_text(x + 1, y + 2, text=texto, font=font,
                       fill="#9dc8ef", tags=tags)
    return canvas.create_text(x, y, text=texto, font=font,
                              fill="#ef4fa0", tags=tags)


def rounded_rect(canvas, x1, y1, x2, y2, r=24, fill="#ffffff",
                 outline="", width=1, tags=None):
    tag = tags or f"rr_{x1}_{y1}_{x2}_{y2}"
    canvas.create_arc(x1, y1, x1 + 2*r, y1 + 2*r, start=90, extent=90,
                      fill=fill, outline=outline, width=width, tags=tag)
    canvas.create_arc(x2 - 2*r, y1, x2, y1 + 2*r, start=0, extent=90,
                      fill=fill, outline=outline, width=width, tags=tag)
    canvas.create_arc(x2 - 2*r, y2 - 2*r, x2, y2, start=270, extent=90,
                      fill=fill, outline=outline, width=width, tags=tag)
    canvas.create_arc(x1, y2 - 2*r, x1 + 2*r, y2, start=180, extent=90,
                      fill=fill, outline=outline, width=width, tags=tag)
    canvas.create_rectangle(x1 + r, y1, x2 - r, y2, fill=fill,
                            outline=outline, width=width, tags=tag)
    canvas.create_rectangle(x1, y1 + r, x2, y2 - r, fill=fill,
                            outline=outline, width=width, tags=tag)
    return tag


def panel(canvas, x1, y1, x2, y2, r=24, fill="#fff8fb"):
    rounded_rect(canvas, x1 + 6, y1 + 8, x2 + 6, y2 + 8, r,
                 fill="#d989b7", outline="")
    return rounded_rect(canvas, x1, y1, x2, y2, r, fill=fill,
                        outline="#f26fb1", width=3)


def boton_texto(canvas, x, y, texto, comando, w=150, h=48,
                fill="#ff9bcc", fg="#ffffff"):
    tag = f"txt_btn_{next(_TAG_COUNTER)}"
    rounded_rect(canvas, x - w//2, y - h//2, x + w//2, y + h//2,
                 18, fill=fill, outline="#f0529e", width=2, tags=tag)
    canvas.create_text(x, y, text=texto, fill=fg,
                       font=(DISPLAY_FONT, 13, "bold"), tags=tag)

    def _enter(_):
        cursor_mano(canvas)

    def _leave(_):
        cursor_normal(canvas)

    def _click(_):
        from utilidades.sonidos import reproducir_click

        reproducir_click()
        comando()

    canvas.tag_bind(tag, "<Enter>", _enter)
    canvas.tag_bind(tag, "<Leave>", _leave)
    canvas.tag_bind(tag, "<Button-1>", _click)
    return tag


def boton_cerrar(canvas, app, x=34, y=32):
    return boton_en_canvas(canvas, x=x, y=y,
                           ruta_img="pantashas/botones/cerrarapp.png",
                           size=(50, 50), comando=app.cerrar)


def navegacion(canvas, app, activo=None, x=728, y=168, dibujar=True):
    botones = [
        ("inicio", "pantashas/botones/inicioboton.PNG", _ir_menu),
        ("diario", "pantashas/botones/diarioboton.PNG", _ir_diario),
        ("gato", "pantashas/botones/gatoboton.PNG", _ir_gato),
        ("closet", "pantashas/botones/closetboton.PNG", _ir_closet),
    ]
    for i, (nombre, ruta, callback) in enumerate(botones):
        yy = y + i * 66
        tag = f"nav_{nombre}_{next(_TAG_COUNTER)}"
        if nombre == activo and dibujar:
            rounded_rect(canvas, x - 55, yy - 25, x + 55, yy + 25,
                         14, fill="#fff5a8", outline="#ff67ad", width=2)
        if dibujar:
            boton_en_canvas(canvas, x=x, y=yy, ruta_img=ruta, size=(96, 46),
                            comando=lambda cb=callback: cb(app))
            continue

        canvas.create_rectangle(x - 50, yy - 24, x + 50, yy + 24,
                                fill="", outline="", tags=tag)
        canvas.tag_bind(tag, "<Enter>", lambda _: cursor_mano(canvas))
        canvas.tag_bind(tag, "<Leave>", lambda _: cursor_normal(canvas))
        canvas.tag_bind(tag, "<Button-1>",
                        lambda _, cb=callback: cb(app))


def _ir_menu(app):
    from pantashas.menu import Menu
    app.cambiar_pantalla(Menu)


def _ir_closet(app):
    from pantashas.closet import Closet
    app.cambiar_pantalla(Closet)


def _ir_diario(app):
    from pantashas.diario import Diario
    app.cambiar_pantalla(Diario)


def _ir_gato(app):
    from pantashas.gato import Gato
    app.cambiar_pantalla(Gato)
