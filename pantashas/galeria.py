import os
import tkinter as tk

from PIL import Image, ImageTk

from utilidades.avatar import descargar_imagen
from utilidades.botonsitos import boton_en_canvas
from utilidades.cargador import Cargador
from utilidades.cursor_app import cursor_mano, cursor_normal
from utilidades.ui import DISPLAY_FONT, boton_cerrar, fondo_suave, navegacion, panel, texto_sombra


class Galeria(tk.Frame):
    def __init__(self, root, app):
        super().__init__(root)
        self.pack(fill="both", expand=True)
        self.app = app
        self.imagenes_refs = []

        self.canvas = tk.Canvas(self, width=800, height=600,
                                highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        fondo_suave(self.canvas, "Mis monitas")
        panel(self.canvas, 74, 88, 650, 552, r=26, fill="#fff8fb")
        texto_sombra(self.canvas, 362, 128, "Toca una foto para descargarla",
                     font=(DISPLAY_FONT, 14, "bold"),
                     fill="#ef4fa0", shadow="#fff8a8")

        self._dibujar_galeria()
        boton_cerrar(self.canvas, self.app)
        navegacion(self.canvas, self.app)

    def _carpeta(self):
        return os.path.join(Cargador.BASE, "datos", "galeria")

    def _dibujar_galeria(self):
        carpeta = self._carpeta()
        os.makedirs(carpeta, exist_ok=True)
        archivos = [a for a in os.listdir(carpeta)
                    if a.lower().endswith((".png", ".jpg", ".jpeg"))]
        archivos.sort(reverse=True)

        if not archivos:
            texto_sombra(self.canvas, 362, 320, "Aun no hay avatares guardados",
                         font=(DISPLAY_FONT, 13, "bold"),
                         fill="#8b5d7a", shadow="#fff8fd")
            return

        cols = 3
        x0, y0 = 168, 236
        gap_x, gap_y = 168, 190
        for i, archivo in enumerate(archivos[:6]):
            ruta = os.path.join(carpeta, archivo)
            col = i % cols
            fila = i // cols
            x = x0 + col * gap_x
            y = y0 + fila * gap_y
            self._tarjeta(ruta, x, y)

    def _tarjeta(self, ruta, x, y):
        panel(self.canvas, x - 62, y - 88, x + 62, y + 86, r=18, fill="#ffffff")
        img = Image.open(ruta).convert("RGBA")
        img.thumbnail((104, 138), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        self.imagenes_refs.append(photo)
        item = self.canvas.create_image(x, y - 10, image=photo, anchor="center")
        texto_sombra(self.canvas, x, y + 66, "Descargar",
                     font=(DISPLAY_FONT, 8, "bold"),
                     fill="#ef4fa0", shadow="#fff8fd")
        self.canvas.tag_bind(item, "<Enter>",
                             lambda _: cursor_mano(self.canvas))
        self.canvas.tag_bind(item, "<Leave>",
                             lambda _: cursor_normal(self.canvas))
        self.canvas.tag_bind(item, "<Button-1>",
                             lambda _, r=ruta: self._descargar(r))

    def _descargar(self, ruta):
        destino = descargar_imagen(ruta)
        self.canvas.delete("msg_galeria")
        texto_sombra(self.canvas, 362, 570, f"Descargada: {destino}",
                     font=(DISPLAY_FONT, 8, "bold"),
                     fill="#ef4fa0", shadow="#fff8a8", tags="msg_galeria")
        self.after(2500, lambda: self.canvas.delete("msg_galeria"))
