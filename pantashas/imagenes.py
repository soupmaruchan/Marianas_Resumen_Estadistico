import tkinter as tk

from utilidades.botonsitos import boton_en_canvas
from utilidades.ui import (
    DISPLAY_FONT,
    boton_cerrar,
    fondo_suave,
    navegacion,
    panel,
    texto_sombra,
    titulo_revista,
)


class Imagenes(tk.Frame):
    def __init__(self, root, app):
        super().__init__(root)
        self.pack(fill="both", expand=True)
        self.app = app

        self.canvas = tk.Canvas(self, width=800, height=600, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        fondo_suave(self.canvas)
        titulo_revista(self.canvas, 400, 70, "Galeria Magica")
        panel(self.canvas, 150, 126, 620, 524, r=28, fill="#fff8fb")
        texto_sombra(self.canvas, 385, 220, "Outfits fuera de este mundo",
                     font=(DISPLAY_FONT, 20, "bold"),
                     fill="#ef4fa0", shadow="#fff8a8")
        texto_sombra(self.canvas, 385, 258, "Guarda tus monitas y bajalas cuando quieras.",
                     font=(DISPLAY_FONT, 10, "bold"),
                     fill="#8b5d7a", shadow="#fff8fd")

        boton_en_canvas(self.canvas, x=385, y=354,
                        ruta_img="pantashas/iconosystickers/carpetaimagenes.png",
                        size=(120, 120), comando=self._abrir_galeria)

        texto_sombra(self.canvas, 385, 441, "Abrir galeria",
                     font=(DISPLAY_FONT, 13, "bold"),
                     fill="#ef4fa0", shadow="#fff8a8")

        boton_cerrar(self.canvas, self.app)
        navegacion(self.canvas, self.app)

    def _abrir_galeria(self):
        from pantashas.galeria import Galeria
        self.app.cambiar_pantalla(Galeria)
