from utilidades.cargador import Cargador
from utilidades.cursor_app import cursor_mano, cursor_normal
from utilidades.sonidos import reproducir_click


def boton_en_canvas(canvas, x, y, ruta_img, size, comando,
                    ruta_hover=None, anchor="center"):
    img_normal = Cargador.imagen(ruta_img, size)
    img_hover = Cargador.imagen(ruta_hover, size) if ruta_hover else img_normal

    if img_normal is None:
        return None

    item_id = canvas.create_image(x, y, image=img_normal, anchor=anchor)
    tag = f"btn_{item_id}"
    canvas.addtag_withtag(tag, item_id)

    def _enter(_):
        cursor_mano(canvas)
        canvas.itemconfig(item_id, image=img_hover)

    def _leave(_):
        cursor_normal(canvas)
        canvas.itemconfig(item_id, image=img_normal)

    def _click(_):
        reproducir_click()
        if comando:
            comando()

    canvas.tag_bind(tag, "<Enter>", _enter)
    canvas.tag_bind(tag, "<Leave>", _leave)
    canvas.tag_bind(tag, "<Button-1>", _click)

    return item_id
