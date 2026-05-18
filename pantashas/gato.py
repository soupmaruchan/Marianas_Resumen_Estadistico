import random
import tkinter as tk

from utilidades.botonsitos import boton_en_canvas
from utilidades.cargador import Cargador
from utilidades.cursor_app import cursor_mano, cursor_normal
from utilidades.sonidos import reproducir_magia
from utilidades.ui import (
    DISPLAY_FONT,
    boton_cerrar,
    boton_texto,
    fondo_imagen,
    navegacion,
    titulo_revista,
)


GP = "pantashas/imagenesgato"

TABLERO_CX, TABLERO_CY = 400, 318
TABLERO_SIZE = 258
PIEZA_SIZE = (36, 36)
HIT_SIZE = 54

CELDAS_X = [306, TABLERO_CX, 494]
CELDAS_Y = [235, TABLERO_CY, 397]

CELDAS_XY = [
    (x, y) for y in CELDAS_Y for x in CELDAS_X
]

GANADORAS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]

JUGADORA = "J"
COMPUTADORA = "C"


class Gato(tk.Frame):
    def __init__(self, root, app):
        super().__init__(root)
        self.pack(fill="both", expand=True)
        self.app = app

        self.canvas = tk.Canvas(self, width=800, height=600, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.modo = None
        self._pieza_items = []
        self._estado = [None] * 9
        self._turno_jugadora = True
        self._partida_activa = False
        self._label_msg = None

        self._dibujar_selector_modo()

    def _dibujar_base(self):
        self.canvas.delete("all")
        fondo_imagen(self.canvas, "pantashas/fondos/pantalla_grid.PNG")
        titulo_revista(self.canvas, 400, 88, "Gato Cute", size=24)
        boton_cerrar(self.canvas, self.app)
        navegacion(self.canvas, self.app, activo="gato",
                   x=728, y=188, dibujar=False)

    def _dibujar_selector_modo(self):
        self._dibujar_base()
        self._partida_activa = False
        self._label_msg = None
        self.canvas.create_text(
            400, 226, text="Modo:",
            font=(DISPLAY_FONT, 24, "bold"), fill="#ef4fa0")
        boton_texto(self.canvas, 400, 318, "Solitario",
                    lambda: self._iniciar("solitario"),
                    w=226, h=60, fill="#ff8fc6")
        boton_texto(self.canvas, 400, 396, "Dos jugadores",
                    lambda: self._iniciar("dos"),
                    w=226, h=60, fill="#ff8fc6")

    def _iniciar(self, modo):
        self.modo = modo
        self._dibujar_juego()

    def _dibujar_juego(self):
        self._dibujar_base()

        tablero_img = Cargador.imagen(f"{GP}/Asterisco.PNG", (TABLERO_SIZE, TABLERO_SIZE))
        if tablero_img:
            self.canvas.create_image(TABLERO_CX, TABLERO_CY,
                                     image=tablero_img, anchor="center")

        self._img_flor = Cargador.imagen(f"{GP}/Flor_circulo.PNG", PIEZA_SIZE)
        self._img_estrella = Cargador.imagen(f"{GP}/Estrella_tacha.PNG", PIEZA_SIZE)

        self._reiniciar_estado()

        self._label_msg = self.canvas.create_text(
            400, 518, text=self._texto_turno(),
            font=(DISPLAY_FONT, 12, "bold"), fill="#ef4fa0")

        self._bind_celdas()

        boton_en_canvas(self.canvas, x=400, y=554,
                        ruta_img="pantashas/botones/ok.png",
                        size=(72, 72), comando=self._reiniciar)

    def _bind_celdas(self):
        for i, (cx, cy) in enumerate(CELDAS_XY):
            area = self.canvas.create_rectangle(
                cx - HIT_SIZE//2, cy - HIT_SIZE//2,
                cx + HIT_SIZE//2, cy + HIT_SIZE//2,
                fill="", outline="", tags=f"celda_{i}")
            self.canvas.tag_bind(area, "<Button-1>",
                                 lambda _, idx=i: self._click_tablero(idx))
            self.canvas.tag_bind(area, "<Enter>",
                                 lambda _: cursor_mano(self.canvas))
            self.canvas.tag_bind(area, "<Leave>",
                                     lambda _: cursor_normal(self.canvas))

    def _click_tablero(self, idx):
        if self.modo == "dos" and not self._turno_jugadora:
            self._click_celda_jugador2(idx)
        else:
            self._click_celda(idx)

    def _click_celda(self, idx):
        if not self._partida_activa or not self._turno_jugadora:
            return
        if self._estado[idx] is not None:
            return
        self._colocar(idx, JUGADORA)
        if self._revisar_fin():
            return

        if self.modo == "dos":
            self._turno_jugadora = False
            self.canvas.itemconfig(self._label_msg, text=self._texto_turno())
            return

        self._turno_jugadora = False
        self.canvas.itemconfig(self._label_msg, text="Pensando...")
        self.after(500, self._turno_computadora)

    def _click_celda_jugador2(self, idx):
        if not self._partida_activa or self._turno_jugadora:
            return
        if self._estado[idx] is not None:
            return
        self._colocar(idx, COMPUTADORA)
        if self._revisar_fin():
            return
        self._turno_jugadora = True
        self.canvas.itemconfig(self._label_msg, text=self._texto_turno())

    def _turno_computadora(self):
        idx = self._elegir_computadora()
        if idx is not None:
            self._colocar(idx, COMPUTADORA)
        self._revisar_fin()
        if self._partida_activa:
            self._turno_jugadora = True
            self.canvas.itemconfig(self._label_msg, text="Tu turno: coloca una flor")

    def _elegir_computadora(self):
        libres = [i for i, v in enumerate(self._estado) if v is None]
        if not libres:
            return None
        for idx in libres:
            self._estado[idx] = COMPUTADORA
            if self._hay_ganador() == COMPUTADORA:
                self._estado[idx] = None
                return idx
            self._estado[idx] = None
        for idx in libres:
            self._estado[idx] = JUGADORA
            if self._hay_ganador() == JUGADORA:
                self._estado[idx] = None
                return idx
            self._estado[idx] = None
        if self._estado[4] is None:
            return 4
        return random.choice(libres)

    def _colocar(self, idx, jugador):
        self._estado[idx] = jugador
        cx, cy = CELDAS_XY[idx]
        img = self._img_flor if jugador == JUGADORA else self._img_estrella
        if img:
            iid = self.canvas.create_image(cx, cy, image=img, anchor="center")
            self._pieza_items.append(iid)
        reproducir_magia()

    def _hay_ganador(self):
        for a, b, c in GANADORAS:
            if (self._estado[a] is not None and
                    self._estado[a] == self._estado[b] == self._estado[c]):
                return self._estado[a]
        return None

    def _revisar_fin(self):
        ganador = self._hay_ganador()
        if ganador == JUGADORA:
            self.canvas.itemconfig(self._label_msg, text="Gana la flor!")
            self._partida_activa = False
            return True
        if ganador == COMPUTADORA:
            texto = "Gana la estrella!" if self.modo == "dos" else "Gano la computadora"
            self.canvas.itemconfig(self._label_msg, text=texto)
            self._partida_activa = False
            return True
        if all(v is not None for v in self._estado):
            self.canvas.itemconfig(self._label_msg, text="Empate!")
            self._partida_activa = False
            return True
        return False

    def _reiniciar(self):
        for iid in self._pieza_items:
            self.canvas.delete(iid)
        self._reiniciar_estado()
        self.canvas.itemconfig(self._label_msg, text=self._texto_turno())

    def _reiniciar_estado(self):
        self._pieza_items = []
        self._estado = [None] * 9
        self._turno_jugadora = True
        self._partida_activa = True

    def _texto_turno(self):
        if self.modo == "dos":
            return "Turno flor" if self._turno_jugadora else "Turno estrella"
        return "Tu turno: coloca una flor"
