import os

from PIL import Image

from utilidades.cargador import Cargador


_cursor_cache = None


def cursor_normal(canvas):
    try:
        canvas.config(cursor=_cursor_personalizado())
    except Exception:
        canvas.config(cursor="arrow")


def cursor_mano(canvas):
    try:
        canvas.config(cursor="hand2")
    except Exception:
        pass


def _cursor_personalizado():
    global _cursor_cache
    if _cursor_cache is not None:
        return _cursor_cache

    try:
        carpeta = os.path.join(Cargador.BASE, "datos", "cursor")
        os.makedirs(carpeta, exist_ok=True)
        source = os.path.join(carpeta, "flecha.xbm")
        mask = os.path.join(carpeta, "flecha_mask.xbm")

        if not os.path.exists(source) or not os.path.exists(mask):
            img = Image.open(Cargador.ruta("pantashas/iconosystickers/iconoflecha.png"))
            img = img.convert("RGBA")
            img.thumbnail((30, 30), Image.LANCZOS)

            cursor = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
            cursor.alpha_composite(img, (1, 1))
            alpha = cursor.getchannel("A")

            _guardar_xbm(source, "flecha", alpha)
            _guardar_xbm(mask, "flecha_mask", alpha)

        src = source.replace("\\", "/")
        msk = mask.replace("\\", "/")
        _cursor_cache = f"@{{{src}}} {{{msk}}} #ef4fa0 white"
    except Exception:
        _cursor_cache = "arrow"

    return _cursor_cache


def _guardar_xbm(ruta, nombre, alpha):
    width, height = alpha.size
    pixels = alpha.load()
    bytes_por_fila = (width + 7) // 8
    datos = []

    for y in range(height):
        for byte_idx in range(bytes_por_fila):
            valor = 0
            for bit in range(8):
                x = byte_idx * 8 + bit
                if x < width and pixels[x, y] > 20:
                    valor |= 1 << bit
            datos.append(valor)

    with open(ruta, "w", encoding="ascii") as f:
        f.write(f"#define {nombre}_width {width}\n")
        f.write(f"#define {nombre}_height {height}\n")
        f.write(f"#define {nombre}_x_hot 2\n")
        f.write(f"#define {nombre}_y_hot 2\n")
        f.write(f"static unsigned char {nombre}_bits[] = {{\n")
        for i, valor in enumerate(datos):
            sep = "," if i < len(datos) - 1 else ""
            f.write(f"  0x{valor:02x}{sep}")
            f.write("\n" if (i + 1) % 12 == 0 else " ")
        f.write("\n};\n")
