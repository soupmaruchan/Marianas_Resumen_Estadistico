import tkinter as tk

from utilidades.cargador import Cargador
from utilidades.cursor_app import cursor_mano, cursor_normal
from utilidades.sonidos import reproducir_click
from utilidades.ui import boton_cerrar


class Inicio(tk.Frame):
    def __init__(self, root, app):
        super().__init__(root)
        self.pack(fill="both", expand=True)
        self.app = app

        self.canvas = tk.Canvas(self, width=800, height=600, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        cursor_normal(self.canvas)

        bg = Cargador.imagen("pantashas/inicioo/Pantallainicio.PNG", (800, 600))
        if bg:
            self.canvas.create_image(0, 0, image=bg, anchor="nw")

        start_area = self.canvas.create_rectangle(
            250, 260, 550, 410, fill="", outline="")
        self.canvas.tag_bind(start_area, "<Button-1>", self._click_start)
        self.canvas.tag_bind(start_area, "<Enter>",
                             lambda _: cursor_mano(self.canvas))
        self.canvas.tag_bind(start_area, "<Leave>",
                             lambda _: cursor_normal(self.canvas))
        boton_cerrar(self.canvas, self.app)

    def _click_start(self, _):
        reproducir_click()
        self._entrar()

    def _entrar(self):
        from pantashas.menu import Menu
        self.app.cambiar_pantalla(Menu)
