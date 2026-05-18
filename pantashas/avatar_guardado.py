import tkinter as tk

from PIL import ImageTk

from utilidades.avatar import componer_avatar, descargar_imagen, guardar_avatar_en_galeria
from utilidades.botonsitos import boton_en_canvas
from utilidades.ui import (
    DISPLAY_FONT,
    boton_cerrar,
    boton_texto,
    fondo_suave,
    navegacion,
    panel,
    texto_sombra,
)


class AvatarGuardado(tk.Frame):
    def __init__(self, root, app, outfit):
        super().__init__(root)
        self.pack(fill="both", expand=True)
        self.app = app
        self.outfit = outfit
        self._ruta_guardada = None
        self._avatar_photo = None

        self.canvas = tk.Canvas(self, width=800, height=600, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        fondo_suave(self.canvas, "Tu avatar quedo precioso")
        panel(self.canvas, 150, 82, 455, 560, r=28, fill="#fff8fb")
        panel(self.canvas, 475, 142, 650, 482, r=24, fill="#ffe1f0")

        avatar = componer_avatar(self.outfit, (250, 460))
        self._avatar_photo = ImageTk.PhotoImage(avatar)
        self.canvas.create_image(304, 326, image=self._avatar_photo, anchor="center")

        texto_sombra(self.canvas, 562, 198, "Guardar",
                     font=(DISPLAY_FONT, 18, "bold"),
                     fill="#ef4fa0", shadow="#fff8a8")
        texto_sombra(self.canvas, 562, 229, "en la app o en tu compu",
                     font=(DISPLAY_FONT, 10, "bold"),
                     fill="#8b5d7a", shadow="#fff8fd")

        boton_en_canvas(self.canvas, x=562, y=302,
                        ruta_img="pantashas/iconosystickers/carpetaimagenes.png",
                        size=(88, 88), comando=self._guardar_en_app)

        boton_texto(self.canvas, 562, 388, "Descargar",
                    self._descargar, w=136, h=44, fill="#ff8fc6")

        boton_cerrar(self.canvas, self.app)
        navegacion(self.canvas, self.app, activo="closet")

    def _guardar_en_app(self):
        self._ruta_guardada = guardar_avatar_en_galeria(self.outfit)
        self._mensaje("Guardado en galeria")

    def _descargar(self):
        if self._ruta_guardada is None:
            self._guardar_en_app()
        destino = descargar_imagen(self._ruta_guardada)
        self._mensaje(f"Descargado: {destino}")

    def _mensaje(self, texto):
        self.canvas.delete("msg_avatar")
        texto_sombra(self.canvas, 400, 572, texto,
                     font=(DISPLAY_FONT, 9, "bold"),
                     fill="#ef4fa0", shadow="#fff8a8", tags="msg_avatar")
        self.after(2400, lambda: self.canvas.delete("msg_avatar"))
