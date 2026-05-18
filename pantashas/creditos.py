import tkinter as tk

from utilidades.botonsitos import boton_en_canvas
from utilidades.ui import (
    DISPLAY_FONT,
    boton_cerrar,
    fondo_imagen,
    rounded_rect,
    texto_sombra,
)


class Creditos(tk.Frame):
    def __init__(self, root, app):
        super().__init__(root)
        self.pack(fill="both", expand=True)
        self.app = app

        self.canvas = tk.Canvas(self, width=800, height=600, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        fondo_imagen(self.canvas, "pantashas/fondos/menu_principal.png")
        self._panel_creditos()
        boton_cerrar(self.canvas, self.app)
        boton_en_canvas(self.canvas, x=260, y=220,
                        ruta_img="pantashas/iconosystickers/iconoflecha.png",
                        size=(36, 36), comando=self._volver_menu)

    def _panel_creditos(self):
        rounded_rect(self.canvas, 206, 184, 594, 538, r=28,
                     fill="#fff7bf", outline="#ef4fa0", width=4)
        rounded_rect(self.canvas, 222, 206, 578, 516, r=22,
                     fill="#fffdf4", outline="#9dc8ef", width=3)

        creditos = [
            ("Arte y Diseño UX",
             "Esthela Naomi Oroz Leal\nElena Yaretzi Ochoa Jarrillo"),
            ("Programacion y desarrollo del codigo",
             "Mariana Fabiola Cisneros Garcia"),
            ("Conceptualizacion y metodologia",
             "Jennifer Atziri Mariscal Magaña"),
        ]

        y = 264
        for titulo, nombres in creditos:
            texto_sombra(self.canvas, 400, y, titulo,
                         font=(DISPLAY_FONT, 12, "bold"),
                         fill="#ef4fa0", shadow="#fff8a8")
            self.canvas.create_text(400, y + 34, text=nombres,
                                    font=(DISPLAY_FONT, 11, "bold"),
                                    fill="#6b3a4a", justify="center")
            y += 92 if "\n" in nombres else 82

        texto_sombra(self.canvas, 400, 680, "Pretty Cute Closet",
                     font=(DISPLAY_FONT, 10, "bold"),
                     fill="#9dc8ef", shadow="#fff8fd")

    def _volver_menu(self):
        from pantashas.menu import Menu
        self.app.cambiar_pantalla(Menu)
