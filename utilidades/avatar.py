import os
import shutil
from datetime import datetime

from PIL import Image

from utilidades.cargador import Cargador


CP = "pantashas/imagenescloset"
PRENDAS = f"{CP}/prendas_estesi"

ORDEN_CAPAS = [
    "cuerpo",
    "calcetas",
    "abajo",
    "blusa",
    "accesorio",
    "zapatos",
    "boca",
    "cejas",
    "ojos",
    "rubor",
    "pelo",
]


def componer_avatar(outfit, size=(250, 460)):
    base = Image.new("RGBA", size, (0, 0, 0, 0))
    for capa in ORDEN_CAPAS:
        nombre = outfit.get(capa)
        if not nombre:
            continue

        if capa in {"blusa", "abajo", "accesorio", "calcetas", "zapatos"}:
            img = Cargador.imagen_pil(f"{PRENDAS}/{nombre}")
            if img is not None:
                _pegar_prenda(base, img, capa, nombre)
            continue

        img = Cargador.imagen_pil(f"{CP}/{nombre}")
        if img is None:
            continue
        img = img.resize(size, Image.LANCZOS)
        base = Image.alpha_composite(base, img)
    return base


def guardar_avatar_en_galeria(outfit):
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    carpeta = os.path.join(base, "datos", "galeria")
    os.makedirs(carpeta, exist_ok=True)
    nombre = f"avatar_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    ruta = os.path.join(carpeta, nombre)
    componer_avatar(outfit, (750, 1380)).save(ruta)
    return ruta


def descargar_imagen(ruta):
    destino_base = os.path.join(os.path.expanduser("~"), "Downloads", "PrettyCuteCloset")
    os.makedirs(destino_base, exist_ok=True)
    destino = os.path.join(destino_base, os.path.basename(ruta))
    shutil.copy2(ruta, destino)
    return destino


def _pegar_prenda(base, img, capa, nombre):
    if img.size[0] > 400 and img.size[1] > 800:
        img = img.resize(base.size, Image.LANCZOS)
        base.alpha_composite(img, (0, 0))
        return

    bw, bh = base.size
    ajuste = _ajuste_prenda(capa, nombre, bw, bh)
    if len(ajuste) == 3:
        cx, cy, escala_w = ajuste
        escala_h = escala_w
    else:
        cx, cy, escala_w, escala_h = ajuste
    base_ref = min(bw, bh)
    target_w = max(1, int(base_ref * escala_w))
    target_h = max(1, int(base_ref * escala_h))
    img = img.resize((target_w, target_h), Image.LANCZOS)
    x = int(cx - target_w / 2)
    y = int(cy - target_h / 2)
    base.alpha_composite(img, (x, y))


def _ajuste_prenda(capa, nombre, bw, bh):
    if capa == "blusa":
        if nombre.startswith("Ropita_25") or nombre.startswith("Ropita_26"):
            return bw * 0.50, bh * 0.515, 0.62
        return bw * 0.50, bh * 0.525, 0.58

    if capa == "abajo":
        if nombre.startswith("pantalon3") or nombre.startswith("pantalon4"):
            return bw * 0.50, bh * 0.700, 0.66, 0.82
        if nombre.startswith("pantalon"):
            return bw * 0.50, bh * 0.695, 0.66, 0.78
        if nombre.startswith("short"):
            return bw * 0.50, bh * 0.635, 0.68, 0.52
        if nombre.startswith("falda2"):
            return bw * 0.50, bh * 0.685, 0.72, 0.70
        return bw * 0.50, bh * 0.640, 0.74, 0.56

    if capa == "calcetas":
        return bw * 0.50, bh * 0.805, 0.39, 0.58

    if capa == "zapatos":
        return bw * 0.50, bh * 0.915, 0.46, 0.34

    if nombre.startswith("Ropita_27"):
        return bw * 0.50, bh * 0.535, 0.64
    if "cadera" in nombre:
        return bw * 0.54, bh * 0.200, 0.38
    return bw * 0.58, bh * 0.505, 0.45
