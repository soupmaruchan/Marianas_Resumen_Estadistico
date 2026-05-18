import winsound


def reproducir_click():
    try:
        winsound.Beep(760, 22)
    except Exception:
        pass


def reproducir_magia():
    try:
        winsound.Beep(1046, 28)
        winsound.Beep(1318, 34)
    except Exception:
        pass
