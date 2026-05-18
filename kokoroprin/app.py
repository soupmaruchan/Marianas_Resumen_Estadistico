class App:
    def __init__(self, root):
        self.root = root
        self.current_screen = None
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar)

    def cambiar_pantalla(self, pantalla, *args, **kwargs):
        if self.current_screen:
            self.current_screen.destroy()

        self.current_screen = pantalla(self.root, self, *args, **kwargs)

    def cerrar(self):
        self.root.destroy()
