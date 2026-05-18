import tkinter as tk

from PIL import Image, ImageTk

from utilidades.avatar import componer_avatar
from utilidades.botonsitos import boton_en_canvas
from utilidades.cargador import Cargador
from utilidades.cursor_app import cursor_mano, cursor_normal
from utilidades.guardado import Guardado
from utilidades.ui import (
    DISPLAY_FONT,
    boton_cerrar,
    boton_texto,
    fondo_imagen,
    navegacion,
    texto_sombra,
    titulo_revista,
)


CP = "pantashas/imagenescloset"
PRENDAS = f"{CP}/prendas_estesi"

CATEGORIAS = [
    {
        "id": "cuerpo",
        "label": "Cuerpo",
        "icono": f"{CP}/Iconopiel.PNG",
        "clave": "cuerpo",
        "items": ["Cuerpo_1.PNG", "Cuerpo_2.PNG", "Cuerpo_3.PNG",
                  "Cuerpo_4.PNG", "Cuerpo_5.PNG"],
        "obligatorio": True,
    },
    {
        "id": "pelo",
        "label": "Cabello",
        "icono": f"{CP}/Iconocabello.PNG",
        "clave": "pelo",
        "items": ["Cabello_01.PNG", "Pelo_02.PNG", "Pelo_03.PNG",
                  "Pelo_04.PNG", "Pelo_05.PNG", "Pelo_06.PNG"],
    },
    {
        "id": "ropa",
        "label": "Ropa",
        "icono": f"{CP}/Iconovarios.PNG",
        "partes": [
            ("blusa", "Blusa", ["blusa_1.png", "blusa_2.png", "blusa_3.png",
                                "blusa_4.png", "blusa_5.png", "blusa_6.png",
                                "blusa_7.png", "chaqueta.png"]),
            ("accesorio", "Accesorio", ["bolsa_1.png", "bolsa_2.png"]),
            ("abajo", "Abajo", ["short_1.png", "falda_1.png", "falda_2.png",
                                "pantalon_1.png", "pantalon_2.png",
                                "pantalon_3.png", "pantalon_4.png"]),
            ("calcetas", "Calcetas", ["calcetas_1.png", "calcetas_2.png",
                                      "calcetas_3.png", "calcetas_4.png",
                                      "calcetas_5.png"]),
            ("zapatos", "Zapatos", ["zapatos_1.png", "zapatos_2.png",
                                    "zapatos_3.png", "zapatos_4.png",
                                    "zapatos_5.png", "zapatos_6.png",
                                    "zapatos_7.png"]),
        ],
    },
    {
        "id": "cejas",
        "label": "Cejas",
        "icono": f"{CP}/Iconoceja.PNG",
        "clave": "cejas",
        "items": ["Ceja_01.PNG", "Ceja_02.PNG", "Ceja_03.PNG",
                  "Ceja_04.PNG", "Ceja_05.PNG", "Ceja_06.PNG"],
    },
    {
        "id": "ojos",
        "label": "Ojos",
        "icono": f"{CP}/Iconoojo.PNG",
        "clave": "ojos",
        "items": ["Ojos_1.PNG", "Ojos_2.PNG", "Ojos_3.PNG",
                  "Ojos_4.PNG", "Ojos_5.PNG"],
    },
    {
        "id": "boca",
        "label": "Boca",
        "icono": f"{CP}/Iconoboca.PNG",
        "clave": "boca",
        "items": ["Boca_1.PNG", "Boca_2.PNG", "Boca_3.PNG", "Boca_4.PNG",
                  "Boca_5.PNG", "Boca_6.PNG", "Boca_7.PNG"],
    },
    {
        "id": "rubor",
        "label": "Rubor",
        "icono": f"{CP}/Iconorubor.PNG",
        "clave": "rubor",
        "items": ["Rubor_1.PNG", "Rubor_2.PNG", "Rubor3.PNG",
                  "Rubor_4.PNG", "Rubor_5.PNG", "Rubor_6.PNG", "Rubor_7.PNG"],
    },
]

CHAR_SIZE = (218, 398)
CHAR_X, CHAR_Y = 240, 312
CATEGORY_X_START = 126
CATEGORY_Y = 104
CATEGORY_GAP = 39
CATEGORY_ICON_SIZE = 31
CATEGORY_HIGHLIGHT = 21
FLECHA_OFFSET = 104

CONTROL_POS = {
    "cuerpo": (CHAR_X, 494),
    "pelo": (CHAR_X, 188),
    "cejas": (CHAR_X, 220),
    "ojos": (CHAR_X, 252),
    "rubor": (CHAR_X, 280),
    "boca": (CHAR_X, 312),
}

ROPA_CONTROL_POS = {
    "blusa": (CHAR_X, 276),
    "accesorio": (CHAR_X, 322),
    "abajo": (CHAR_X, 368),
    "calcetas": (CHAR_X, 424),
    "zapatos": (CHAR_X, 486),
}


class Closet(tk.Frame):
    def __init__(self, root, app):
        super().__init__(root)
        self.pack(fill="both", expand=True)
        self.app = app
        self.outfit = self._normalizar_outfit({"cuerpo": "Cuerpo_1.PNG"})
        self.cat_idx = 0
        self._char_photo = None
        self._control_tags = []
        self._decor_refs = []

        self.canvas = tk.Canvas(self, width=800, height=600, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        fondo_imagen(self.canvas, f"{CP}/Pantalla_closet.PNG")
        titulo_revista(self.canvas, 380, 62, "Pretty Cute Closet", size=25)
        self._decorar_closet()
        self._char_item = self.canvas.create_image(CHAR_X, CHAR_Y, anchor="center")
        self._build_iconos_categoria()
        self._actualizar_personaje()
        self._mostrar_controles()

        boton_cerrar(self.canvas, self.app)
        navegacion(self.canvas, self.app, activo="closet",
                   x=728, y=188, dibujar=False)
        boton_en_canvas(self.canvas, x=520, y=552,
                        ruta_img="pantashas/botones/ok.png",
                        size=(78, 78), comando=self._guardar_y_ver_avatar)

    def _normalizar_outfit(self, outfit):
        outfit.setdefault("cuerpo", "Cuerpo_1.PNG")
        for clave in ["pelo", "cejas", "ojos", "boca", "rubor",
                      "blusa", "abajo", "accesorio", "calcetas", "zapatos"]:
            outfit.setdefault(clave, None)
        outfit.pop("ropita", None)
        for cat in CATEGORIAS:
            if "partes" in cat:
                for clave, _, items in cat["partes"]:
                    outfit[clave] = self._normalizar_nombre(outfit.get(clave), items)
                continue
            outfit[cat["clave"]] = self._normalizar_nombre(
                outfit.get(cat["clave"]), cat["items"])
        return outfit

    def _normalizar_nombre(self, actual, items):
        if not actual:
            return None
        for item in items:
            if actual.lower() == item.lower():
                return item
        return None

    def _decorar_closet(self):
        decor = [
            ("blusa_1.png", 454, 180, (92, 118)),
            ("blusa_3.png", 532, 180, (92, 118)),
            ("blusa_5.png", 610, 180, (96, 118)),
            ("falda_1.png", 470, 315, (120, 140)),
            ("zapatos_1.png", 470, 500, (68, 56)),
            ("zapatos_3.png", 550, 500, (70, 58)),
            ("zapatos_6.png", 630, 500, (70, 58)),
        ]
        for nombre, x, y, size in decor:
            img = self._preview_prenda(nombre, size)
            if img:
                self._decor_refs.append(img)
                self.canvas.create_image(x, y, image=img, anchor="center")

    def _preview_prenda(self, nombre, size):
        img = Cargador.imagen_pil(f"{PRENDAS}/{nombre}")
        if img is None:
            return None
        bbox = img.getbbox()
        if bbox:
            img = img.crop(bbox)
        img.thumbnail(size, Image.LANCZOS)
        lienzo = Image.new("RGBA", size, (0, 0, 0, 0))
        x = (size[0] - img.width) // 2
        y = (size[1] - img.height) // 2
        lienzo.alpha_composite(img, (x, y))
        return ImageTk.PhotoImage(lienzo)

    def _build_iconos_categoria(self):
        self._icon_ids = []
        x_start = CATEGORY_X_START
        y = CATEGORY_Y
        gap = CATEGORY_GAP
        for i, cat in enumerate(CATEGORIAS):
            x = x_start + i * gap
            img = Cargador.imagen(cat["icono"],
                                  (CATEGORY_ICON_SIZE, CATEGORY_ICON_SIZE))
            if img:
                item_id = self.canvas.create_image(x, y, image=img, anchor="center")
                self._icon_ids.append(item_id)
                self.canvas.tag_bind(item_id, "<Button-1>",
                                     lambda _, idx=i: self._seleccionar_categoria(idx))
                self.canvas.tag_bind(item_id, "<Enter>",
                                     lambda _: cursor_mano(self.canvas))
                self.canvas.tag_bind(item_id, "<Leave>",
                                     lambda _: cursor_normal(self.canvas))

        self._highlight_cat = self.canvas.create_rectangle(
            x_start - CATEGORY_HIGHLIGHT, y - CATEGORY_HIGHLIGHT,
            x_start + CATEGORY_HIGHLIGHT, y + CATEGORY_HIGHLIGHT,
            outline="#ff66aa", width=2, fill="")
        self._mover_highlight_cat()

    def _mover_highlight_cat(self):
        x = CATEGORY_X_START + self.cat_idx * CATEGORY_GAP
        y = CATEGORY_Y
        self.canvas.coords(self._highlight_cat,
                           x - CATEGORY_HIGHLIGHT, y - CATEGORY_HIGHLIGHT,
                           x + CATEGORY_HIGHLIGHT, y + CATEGORY_HIGHLIGHT)

    def _seleccionar_categoria(self, idx):
        self.cat_idx = idx
        self._mover_highlight_cat()
        self._mostrar_controles()

    def _mostrar_controles(self):
        for tag in self._control_tags:
            self.canvas.delete(tag)
        self._control_tags = []

        cat = CATEGORIAS[self.cat_idx]

        if "partes" in cat:
            for clave, label, items in cat["partes"]:
                x, y = ROPA_CONTROL_POS[clave]
                self._crear_flechas(x, y, lambda c=clave, it=items: self._cambiar_item(c, it, -1),
                                    lambda c=clave, it=items: self._cambiar_item(c, it, 1),
                                    label, label_x=158)
            return

        x, y = CONTROL_POS[cat["id"]]
        self._crear_flechas(
            x, y,
            lambda c=cat: self._cambiar_item(c["clave"], c["items"], -1, c.get("obligatorio")),
            lambda c=cat: self._cambiar_item(c["clave"], c["items"], 1, c.get("obligatorio")),
            None,
        )

    def _crear_flechas(self, x, y, cmd_izq, cmd_der, label=None, label_x=None):
        self._control_tags.append(
            boton_texto(self.canvas, x - FLECHA_OFFSET, y, "<", cmd_izq,
                        w=42, h=38, fill="#f35aa7")
        )
        self._control_tags.append(
            boton_texto(self.canvas, x + FLECHA_OFFSET, y, ">", cmd_der,
                        w=42, h=38, fill="#f35aa7")
        )
        if not label:
            return
        tag = f"ctrl_label_{label}"
        texto_sombra(self.canvas, label_x or x, y - 34, label,
                     font=(DISPLAY_FONT, 8, "bold"),
                     fill="#e94f9b", shadow="#fff5a8", tags=tag)
        self._control_tags.append(tag)

    def _cambiar_item(self, clave, items, direccion, obligatorio=False):
        opciones = items if obligatorio else [None] + items
        actual = self.outfit.get(clave)
        if actual not in opciones:
            idx = -1 if direccion > 0 else 0
        else:
            idx = opciones.index(actual)
        self.outfit[clave] = opciones[(idx + direccion) % len(opciones)]
        self._actualizar_personaje()

    def _actualizar_personaje(self):
        avatar = componer_avatar(self.outfit, CHAR_SIZE)
        self._char_photo = ImageTk.PhotoImage(avatar)
        self.canvas.itemconfig(self._char_item, image=self._char_photo)

    def _guardar_y_ver_avatar(self):
        Guardado.guardar_outfit(self.outfit)
        from pantashas.avatar_guardado import AvatarGuardado
        self.app.cambiar_pantalla(AvatarGuardado, dict(self.outfit))
