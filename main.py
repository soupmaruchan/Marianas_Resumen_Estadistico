import sys
import tkinter as tk

sys.dont_write_bytecode = True

from kokoroprin.app import App
from pantashas.inicio import Inicio
from utilidades.cargador import Cargador

root = tk.Tk()
root.geometry("800x600")
root.title("Pretty Cute Closet")
root.resizable(False, False)
try:
    icono = tk.PhotoImage(file=Cargador.ruta("assets/icono_app.png"))
    root.iconphoto(True, icono)
except tk.TclError:
    icono = None


def preparar_ventana(root):
    root.overrideredirect(True)

    def aplicar_esquinas():
        if not sys.platform.startswith("win"):
            return
        try:
            import ctypes

            hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
            region = ctypes.windll.gdi32.CreateRoundRectRgn(0, 0, 800, 600, 28, 28)
            ctypes.windll.user32.SetWindowRgn(hwnd, region, True)
        except Exception:
            pass

    def iniciar_arrastre(event):
        root._drag_activo = event.y_root - root.winfo_y() < 84
        if not root._drag_activo:
            return
        root._drag_x = event.x_root
        root._drag_y = event.y_root
        root._win_x = root.winfo_x()
        root._win_y = root.winfo_y()

    def arrastrar(event):
        if not getattr(root, "_drag_activo", False):
            return
        dx = event.x_root - root._drag_x
        dy = event.y_root - root._drag_y
        root.geometry(f"+{root._win_x + dx}+{root._win_y + dy}")

    root.bind("<ButtonPress-1>", iniciar_arrastre, add="+")
    root.bind("<B1-Motion>", arrastrar, add="+")
    root.after(80, aplicar_esquinas)


preparar_ventana(root)

app = App(root)
app.cambiar_pantalla(Inicio)

root.mainloop()
