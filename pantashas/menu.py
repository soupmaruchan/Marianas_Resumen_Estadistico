import tkinter as tk

from PIL import Image, ImageTk

from utilidades.cargador import Cargador
from utilidades.cursor_app import cursor_mano, cursor_normal
from utilidades.sonidos import reproducir_click
from utilidades.ui import DISPLAY_FONT, boton_cerrar, fondo_imagen, texto_sombra, titulo_revista


class Menu(tk.Frame):
    def __init__(self, root, app):
        super().__init__(root)
        self.pack(fill="both", expand=True)
        self.app = app

        self.canvas = tk.Canvas(self, width=800, height=600, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self._iconos_menu = []

        fondo_imagen(self.canvas, "pantashas/fondos/menu_principal.png")
        titulo_revista(self.canvas, 400, 96, "Pretty Cute Closet", size=24)

        self._opcion(426, 356, "CLOSET", self._ir_closet,
                     "pantashas/iconosystickers_extra/fresa.png")
        self._opcion(426, 398, "DIARIO", self._ir_diario,
                     "pantashas/iconosystickers_extra/iconodiario.png")
        self._opcion(426, 440, "GATO", self._ir_gato,
                     "pantashas/iconosystickers_extra/estrella.png")
        self._opcion(426, 482, "GALERIA", self._ir_imagenes,
                     "pantashas/iconosystickers/carpetaimagenes.png")
        self._opcion(426, 524, "CREDITOS", self._ir_creditos,
                     "pantashas/iconosystickers_extra/bootonamarilloo.png")

        boton_cerrar(self.canvas, self.app)

    def _opcion(self, x, y, texto, comando, icono):
        tag = f"menu_{texto}"
        self.canvas.create_rectangle(x - 148, y - 21, x + 148, y + 21,
                                     fill="", outline="", tags=tag)
        icon_item = self._crear_icono_menu(x - 96, y, icono, tag)
        texto_sombra(self.canvas, x, y, texto,
                     font=(DISPLAY_FONT, 17, "bold"),
                     fill="#ef4fa0", shadow="#fff8fd", tags=tag)

        def _click(_):
            reproducir_click()
            comando()

        self.canvas.tag_bind(tag, "<Enter>", lambda _: cursor_mano(self.canvas))
        self.canvas.tag_bind(tag, "<Leave>", lambda _: cursor_normal(self.canvas))
        self.canvas.tag_bind(tag, "<Button-1>", _click)
        if icon_item:
            self.canvas.tag_bind(icon_item, "<Button-1>", _click)

    def _crear_icono_menu(self, x, y, ruta, tag):
        img = Cargador.imagen_pil(ruta)
        if img is None:
            return None
        bbox = img.getbbox()
        if bbox:
            img = img.crop(bbox)
        img.thumbnail((32, 32), Image.LANCZOS)
        lienzo = Image.new("RGBA", (38, 38), (0, 0, 0, 0))
        lienzo.alpha_composite(img, ((38 - img.width) // 2,
                                     (38 - img.height) // 2))
        photo = ImageTk.PhotoImage(lienzo)
        self._iconos_menu.append(photo)
        item = self.canvas.create_image(x, y, image=photo, anchor="center",
                                        tags=tag)
        return item

    def _ir_closet(self):
        from pantashas.closet import Closet
        self.app.cambiar_pantalla(Closet)

    def _ir_diario(self):
        from pantashas.diario import Diario
        self.app.cambiar_pantalla(Diario)

    def _ir_gato(self):
        from pantashas.gato import Gato
        self.app.cambiar_pantalla(Gato)

    def _ir_imagenes(self):
        from pantashas.imagenes import Imagenes
        self.app.cambiar_pantalla(Imagenes)

    def _ir_creditos(self):
        from pantashas.creditos import Creditos
        self.app.cambiar_pantalla(Creditos)
