import json
import os
import sys


def _base_datos():
    proyecto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if getattr(sys, "frozen", False):
        documentos = os.path.join(os.path.expanduser("~"), "Documents")
        return os.path.join(documentos, "PrettyCuteCloset", "datos")
    return os.path.join(proyecto, "datos")


class Guardado:
    BASE = _base_datos()

    _OUTFIT_DEFAULT = {
        "cuerpo": "Cuerpo_1.PNG",
        "pelo": None,
        "cejas": None,
        "ojos": None,
        "boca": None,
        "rubor": None,
        "blusa": None,
        "abajo": None,
        "accesorio": None,
        "calcetas": None,
        "zapatos": None,
    }

    _DIARIO_DEFAULT = {}
    _DIARIO_IMAGENES_DEFAULT = {}

    _GATO_DEFAULT = {
        "nombre": "Mochi",
        "hambre": 80,
        "felicidad": 80,
        "energia": 80,
        "estado": "idle",
    }

    @classmethod
    def carpeta(cls, *partes):
        ruta = os.path.join(cls.BASE, *partes)
        os.makedirs(ruta, exist_ok=True)
        return ruta
    
    @classmethod
    def _ruta(cls, nombre):
        os.makedirs(cls.BASE, exist_ok=True)
        return os.path.join(cls.BASE, f"{nombre}.json")
    
    @classmethod
    def _leer(cls, nombre, default):
        ruta = cls._ruta(nombre)
        if not os.path.exists(ruta):
            return dict(default)
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                datos = json.load(f)
            for k, v in default.items():
                datos.setdefault(k, v)
            return datos
        except (json.JSONDecodeError, IOError):
            print(f"[Guardado] Error leyendo {nombre}.json; usando default.")
            return dict(default)

    @classmethod
    def _escribir(cls, nombre, datos):
        ruta = cls._ruta(nombre)
        try:
            with open(ruta, "w", encoding="utf-8") as f:
                json.dump(datos, f, ensure_ascii=False, indent=2)
        except IOError as e:
            print(f"[Guardado] Error escribiendo {nombre}.json: {e}")

    @classmethod
    def cargar_outfit(cls):
        return cls._leer("outfit", cls._OUTFIT_DEFAULT)

    @classmethod
    def guardar_outfit(cls, outfit):
        cls._escribir("outfit", outfit)

    @classmethod
    def cargar_diario(cls):
        return cls._leer("diario", cls._DIARIO_DEFAULT)

    @classmethod
    def guardar_entrada(cls, fecha, texto):
        diario = cls.cargar_diario()
        diario[fecha] = texto
        cls._escribir("diario", diario)
    
    @classmethod
    def borrar_entrada(cls, fecha):
        diario = cls.cargar_diario()
        diario.pop(fecha, None)
        cls._escribir("diario", diario)

    @classmethod
    def cargar_diario_imagenes(cls):
        return cls._leer("diario_imagenes", cls._DIARIO_IMAGENES_DEFAULT)

    @classmethod
    def guardar_imagen_diario(cls, fecha, ruta_relativa):
        imagenes = cls.cargar_diario_imagenes()
        imagenes[fecha] = ruta_relativa
        cls._escribir("diario_imagenes", imagenes)
    
    @classmethod
    def borrar_imagen_diario(cls, fecha):
        imagenes = cls.cargar_diario_imagenes()
        imagenes.pop(fecha, None)
        cls._escribir("diario_imagenes", imagenes)
    
    @classmethod
    def cargar_gato(cls):
        return cls._leer("gato", cls._GATO_DEFAULT)

    @classmethod
    def guardar_gato(cls, estado):
        cls._escribir("gato", estado)
