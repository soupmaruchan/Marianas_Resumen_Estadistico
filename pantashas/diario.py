import calendar
import os
import shutil
import tkinter as tk
from datetime import date, timedelta
from tkinter import filedialog

from PIL import Image, ImageOps, ImageTk

from utilidades.botonsitos import boton_en_canvas
from utilidades.cargador import Cargador
from utilidades.cursor_app import cursor_mano, cursor_normal
from utilidades.guardado import Guardado
from utilidades.sonidos import reproducir_click
from utilidades.ui import (
    DISPLAY_FONT,
    boton_cerrar,
    boton_texto,
    navegacion,
    rounded_rect,
    texto_sombra,
)


DP = "pantashas/imagenesdiario"
FRAMES_VOLTEO = [
    f"{DP}/Cambio_hoja_1.PNG",
    f"{DP}/Cambio_hoja_2.PNG",
    f"{DP}/Cambio_hoja_3.PNG",
]
FRAME_DELAY = 85
FOTO_CX, FOTO_CY = 238, 388
FOTO_W, FOTO_H = 206, 124
MESES = [
    "", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre",
]


class Diario(tk.Frame):
    def __init__(self, root, app):
        super().__init__(root)
        self.pack(fill="both", expand=True)
        self.app = app
        self.entradas = Guardado.cargar_diario()
        self.imagenes = Guardado.cargar_diario_imagenes()
        self.fecha_actual = date.today()
        self._animando = False
        self._frame_refs = []
        self._foto_diario = None

        self.canvas = tk.Canvas(self, width=800, height=600, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        cursor_normal(self.canvas)

        self._bg_item = self.canvas.create_image(0, 0, anchor="nw")
        self._mostrar_pagina_estatica()

        self._label_fecha = texto_sombra(
            self.canvas, 552, 126, "", font=(DISPLAY_FONT, 12, "bold"),
            fill="#d85a9a", shadow="#fff8a8")

        self._texto = tk.Text(
            self.canvas,
            width=24, height=12,
            font=(DISPLAY_FONT, 10),
            bg="#fffdf4", fg="#6b3a4a",
            relief="flat", bd=0,
            highlightthickness=0,
            wrap="word",
            insertbackground="#ff85c2",
            padx=0, pady=0,
        )
        self._texto_window = self.canvas.create_window(
            560, 340, window=self._texto, anchor="center")

        boton_texto(self.canvas, 122, 518, "<", self._pagina_anterior,
                    w=42, h=40, fill="#ff8fc6")
        boton_texto(self.canvas, 684, 518, ">", self._pagina_siguiente,
                    w=42, h=40, fill="#ff8fc6")

        boton_en_canvas(self.canvas, x=546, y=536,
                        ruta_img="pantashas/botones/ok.png",
                        size=(66, 66), comando=self._guardar_entrada)

        boton_en_canvas(self.canvas, x=142, y=122,
                        ruta_img="pantashas/iconosystickers/iconoflecha.png",
                        size=(44, 44), comando=self._volver_menu)

        boton_cerrar(self.canvas, self.app)
        navegacion(self.canvas, self.app, activo="diario",
                   x=728, y=188, dibujar=False)
        self._actualizar_fecha_y_texto()

    def _mostrar_pagina_estatica(self):
        bg = Cargador.imagen(f"{DP}/Cambio_hoja_estatico.PNG", (800, 600))
        if bg:
            self._frame_refs = [bg]
            self.canvas.itemconfig(self._bg_item, image=bg)

    def _actualizar_fecha_y_texto(self):
        clave = str(self.fecha_actual)
        self.canvas.itemconfig(self._label_fecha,
                               text=self.fecha_actual.strftime("%d / %m / %Y"))
        self._texto.delete("1.0", "end")
        if clave in self.entradas:
            self._texto.insert("1.0", self.entradas[clave])
        self._dibujar_calendario()
        self._mostrar_imagen_fecha()

    def _dibujar_calendario(self):
        self.canvas.delete("calendario")
        mes = calendar.monthcalendar(self.fecha_actual.year, self.fecha_actual.month)
        x0, y0 = 184, 142
        texto_sombra(self.canvas, 282, 142,
                     f"{MESES[self.fecha_actual.month]} {self.fecha_actual.year}",
                     font=(DISPLAY_FONT, 10, "bold"),
                     fill="#d85a9a", shadow="#fff8a8", tags="calendario")
        dias = ["L", "M", "M", "J", "V", "S", "D"]
        for col, dia in enumerate(dias):
            self.canvas.create_text(x0 + col * 28, y0 + 28, text=dia,
                                    font=(DISPLAY_FONT, 8, "bold"),
                                    fill="#8b5d7a", tags="calendario")

        for fila, semana in enumerate(mes):
            for col, dia in enumerate(semana):
                if dia == 0:
                    continue
                x = x0 + col * 28
                y = y0 + 54 + fila * 23
                tag = f"dia_{dia}"
                if dia == self.fecha_actual.day:
                    self.canvas.create_oval(x - 11, y - 10, x + 11, y + 10,
                                            fill="#fff5a8", outline="#ef4fa0",
                                            width=2, tags=("calendario", tag))
                self.canvas.create_text(x, y, text=str(dia),
                                        font=(DISPLAY_FONT, 8, "bold"),
                                        fill="#6b3a4a", tags=("calendario", tag))
                self.canvas.tag_bind(tag, "<Enter>",
                                     lambda _: cursor_mano(self.canvas))
                self.canvas.tag_bind(tag, "<Leave>",
                                     lambda _: cursor_normal(self.canvas))
                self.canvas.tag_bind(tag, "<Button-1>",
                                     lambda _, d=dia: self._seleccionar_dia(d))

    def _seleccionar_dia(self, dia):
        reproducir_click()
        self._guardar_entrada_silencio()
        self.fecha_actual = date(self.fecha_actual.year, self.fecha_actual.month, dia)
        self._actualizar_fecha_y_texto()

    def _mostrar_imagen_fecha(self):
        self.canvas.delete("diario_img")
        x1 = FOTO_CX - FOTO_W // 2 - 8
        y1 = FOTO_CY - FOTO_H // 2 - 8
        x2 = FOTO_CX + FOTO_W // 2 + 8
        y2 = FOTO_CY + FOTO_H // 2 + 8
        rounded_rect(self.canvas, x1, y1, x2, y2, r=16,
                     fill="#fffef7", outline="#ef7ab4", width=2,
                     tags="diario_img")

        clave = str(self.fecha_actual)
        ruta_rel = self.imagenes.get(clave)
        if not ruta_rel:
            icono = Cargador.imagen("pantashas/iconosystickers/carpetaimagenes.png",
                                    (58, 58))
            if icono:
                self.canvas.create_image(FOTO_CX, FOTO_CY - 8,
                                         image=icono, anchor="center",
                                         tags="diario_img")
            texto_sombra(self.canvas, FOTO_CX, FOTO_CY + 42, "Agrega imagen",
                         font=(DISPLAY_FONT, 10, "bold"),
                         fill="#e78bb6", shadow="#fff8a8",
                         tags="diario_img")
            self._activar_area_imagen()
            return

        ruta = Cargador.ruta(ruta_rel)
        if not os.path.exists(ruta):
            texto_sombra(self.canvas, FOTO_CX, FOTO_CY, "Imagen no encontrada",
                         font=(DISPLAY_FONT, 10, "bold"),
                         fill="#e78bb6", shadow="#fff8a8", tags="diario_img")
            self._activar_area_imagen()
            return

        img = Image.open(ruta).convert("RGBA")
        img = ImageOps.fit(img, (FOTO_W, FOTO_H), Image.LANCZOS)
        self._foto_diario = ImageTk.PhotoImage(img)
        self.canvas.create_image(FOTO_CX, FOTO_CY, image=self._foto_diario,
                                 anchor="center", tags="diario_img")
        self._activar_area_imagen()

    def _activar_area_imagen(self):
        self.canvas.tag_bind("diario_img", "<Enter>",
                             lambda _: cursor_mano(self.canvas))
        self.canvas.tag_bind("diario_img", "<Leave>",
                             lambda _: cursor_normal(self.canvas))
        self.canvas.tag_bind("diario_img", "<Button-1>",
                             lambda _: self._subir_imagen())

    def _animar_volteo(self, callback):
        if self._animando:
            return
        self._animando = True
        self.canvas.itemconfigure(self._texto_window, state="hidden")
        self.canvas.itemconfigure(self._label_fecha, state="hidden")
        self.canvas.delete("diario_img")
        self.canvas.delete("calendario")

        frames = [Cargador.imagen(f, (800, 600)) for f in FRAMES_VOLTEO]
        frames = [f for f in frames if f]

        if not frames:
            callback()
            self._terminar_animacion()
            return

        def mostrar_frame(idx):
            if idx < len(frames):
                self._frame_refs = [frames[idx]]
                self.canvas.itemconfig(self._bg_item, image=frames[idx])
                self.after(FRAME_DELAY, lambda: mostrar_frame(idx + 1))
            else:
                callback()
                self._terminar_animacion()

        mostrar_frame(0)

    def _terminar_animacion(self):
        self._mostrar_pagina_estatica()
        self._actualizar_fecha_y_texto()
        self.canvas.itemconfigure(self._texto_window, state="normal")
        self.canvas.itemconfigure(self._label_fecha, state="normal")
        self._animando = False

    def _guardar_entrada(self):
        self._guardar_entrada_silencio()
        self._mensaje("Guardado")

    def _pagina_anterior(self):
        self._guardar_entrada_silencio()

        def _cambiar():
            self.fecha_actual -= timedelta(days=1)

        self._animar_volteo(_cambiar)

    def _pagina_siguiente(self):
        self._guardar_entrada_silencio()

        def _cambiar():
            self.fecha_actual += timedelta(days=1)

        self._animar_volteo(_cambiar)

    def _guardar_entrada_silencio(self):
        texto = self._texto.get("1.0", "end").strip()
        clave = str(self.fecha_actual)
        if texto:
            Guardado.guardar_entrada(clave, texto)
            self.entradas[clave] = texto
        else:
            Guardado.borrar_entrada(clave)
            self.entradas.pop(clave, None)

    def _subir_imagen(self):
        ruta = filedialog.askopenfilename(
            title="Elige una imagen para tu diario",
            filetypes=[
                ("Imagenes", "*.png *.jpg *.jpeg *.gif *.bmp"),
                ("Todos los archivos", "*.*"),
            ],
        )
        if not ruta:
            return

        carpeta = Guardado.carpeta("diario_imagenes")
        nombre = os.path.basename(ruta).replace(" ", "_")
        destino_nombre = f"{self.fecha_actual}_{nombre}"
        destino = os.path.join(carpeta, destino_nombre)
        shutil.copy2(ruta, destino)
        ruta_rel = os.path.join("datos", "diario_imagenes", destino_nombre)
        Guardado.guardar_imagen_diario(str(self.fecha_actual), ruta_rel)
        self.imagenes[str(self.fecha_actual)] = ruta_rel
        self._mostrar_imagen_fecha()

    def _exportar_texto(self):
        self._guardar_entrada_silencio()
        carpeta = Guardado.carpeta("paginas_texto")
        ruta = os.path.join(carpeta, f"{self.fecha_actual}.txt")
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(self.entradas.get(str(self.fecha_actual), ""))
        self._mensaje("Texto guardado")

    def _mensaje(self, texto):
        self.canvas.delete("msg_ok")
        texto_sombra(self.canvas, 584, 574, texto,
                     font=(DISPLAY_FONT, 9, "bold"),
                     fill="#ff4da6", shadow="#fff8a8", tags="msg_ok")
        self.after(1400, lambda: self.canvas.delete("msg_ok"))

    def _volver_menu(self):
        self._guardar_entrada_silencio()
        from pantashas.menu import Menu
        self.app.cambiar_pantalla(Menu)

    def destroy(self):
        self._guardar_entrada_silencio()
        super().destroy()
