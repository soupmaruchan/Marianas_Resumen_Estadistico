import os
import sys

from PIL import Image, ImageTk


def _base_recursos():
    if getattr(sys, "_MEIPASS", None):
        return sys._MEIPASS
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Cargador:
    _cache = {}
    BASE = _base_recursos()
    @classmethod
    def ruta(cls, ruta_relativa):
        if os.path.isabs(ruta_relativa):
            ruta = ruta_relativa
        else:
            normalizada = os.path.normpath(ruta_relativa)
            if normalizada.lower() == "datos" or normalizada.lower().startswith(
                    f"datos{os.sep}"):
                try:
                    from utilidades.guardado import Guardado

                    candidato = os.path.join(os.path.dirname(Guardado.BASE),
                                             normalizada)
                    if os.path.exists(candidato):
                        return candidato
                except Exception:
                    pass
            ruta = os.path.join(cls.BASE, ruta_relativa)

        if os.path.exists(ruta):
            return ruta

        carpeta, nombre = os.path.split(ruta)
        if os.path.isdir(carpeta):
            nombre_lower = nombre.lower()
            for candidato in os.listdir(carpeta):
                if candidato.lower() == nombre_lower:
                    return os.path.join(carpeta, candidato)

        return ruta

    def imagen(cls, ruta_relativa, size=None):
        clave = (ruta_relativa, size)
        if clave in cls._cache:
            return cls._cache[clave]

        ruta = cls.ruta(ruta_relativa)
        if not os.path.exists(ruta):
            print(f"[Cargador] ADVERTENCIA: no se encontro '{ruta}'")
            return None

        img = Image.open(ruta).convert("RGBA")
        if size:
            img = img.resize(size, Image.LANCZOS)

        photo = ImageTk.PhotoImage(img)
        cls._cache[clave] = photo
        return photo

    def imagen_pil(cls, ruta_relativa, size=None):
        ruta = cls.ruta(ruta_relativa)
        if not os.path.exists(ruta):
            print(f"[Cargador] ADVERTENCIA: no se encontro '{ruta}'")
            return None

        img = Image.open(ruta).convert("RGBA")
        if size:
            img = img.resize(size, Image.LANCZOS)
        return img

    def limpiar_cache(cls):
        cls._cache.clear()
