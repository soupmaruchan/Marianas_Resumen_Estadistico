# =========================================================
# GENERADOR DE ARTE ASCII ANIMADO
# =========================================================

import os
import time
import random

# =========================================================
# PALETA DE COLORSITOS
# =========================================================

RESET = "\033[0m"

ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"

PASTEL_ROSA = "\033[38;5;218m"
PASTEL_LILA = "\033[38;5;183m"
PASTEL_AZUL = "\033[38;5;153m"
PASTEL_MENTA = "\033[38;5;121m"
PASTEL_AMARILLO = "\033[38;5;229m"
PASTEL_DURAZNO = "\033[38;5;216m"

MAGENTA = "\033[35m"
ROJO = "\033[31m"
VERDE = "\033[32m"

CAFE = "\033[38;5;94m"

COLOR_INPUT = "\033[38;5;222m"

# =========================================================
# GALERIA
# =========================================================

galeria = []


# =========================================================
# LIMPIAR TERMINAL
# =========================================================

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


# =========================================================
# LLUVIA DE ESTRELLAS
# =========================================================

def lluvia_inicio():

    simbolos = ["✦","⋆","✧","✩","✶"]

    for _ in range(25):

        limpiar()

        for i in range(20):

            linea=""

            for j in range(70):

                if random.random()<0.04:
                    linea+=random.choice(simbolos)
                else:
                    linea+=" "

            print(PASTEL_LILA+linea+RESET)

        time.sleep(0.08)


# =========================================================
# TITULO MULTICOLOR
# =========================================================

def titulo():

    print(PASTEL_ROSA+"╔══════════════════════════════════════╗"+RESET)

    print(
        PASTEL_ROSA+"║ "+
        PASTEL_LILA+"G"+
        PASTEL_AZUL+"A"+
        PASTEL_MENTA+"L"+
        PASTEL_AMARILLO+"E"+
        PASTEL_DURAZNO+"R"+
        PASTEL_LILA+"I"+
        PASTEL_AZUL+"A"+
        RESET+" ASCII                        ║"
    )
    print(PASTEL_ROSA+"╚══════════════════════════════════════╝"+RESET)
# =========================================================
# TABLA MULTIPLKICARS
# =========================================================
def tabla_visual():

    limpiar()

    numero = int(input("Número de la tabla: "))

    print("╔════════════════════╗")
    print(f"║   TABLA DEL {numero}      ║")
    print("╠════════════════════╣")

    for i in range(1,11):

        resultado = numero*i

        print(f"║ {numero} x {i} = {resultado:<3}       ║")

    print("╚════════════════════╝")

    input("Enter")

# =========================================================
# PATRONES GEOMETRICOS
# =========================================================

def generar_triangulo(altura):

    arte = ""

    for i in range(1,altura+1):

        arte += PASTEL_AMARILLO + "*"*i + RESET + "\n"

    return arte


def generar_cuadrado(lado):

    arte=""

    for i in range(lado):

        if i==0 or i==lado-1:
            arte+=PASTEL_AZUL+"█"*lado+RESET+"\n"

        else:
            arte+=PASTEL_AZUL+"█"+RESET+" "*(lado-2)+PASTEL_AZUL+"█"+RESET+"\n"

    return arte


def generar_piramide(altura):

    arte=""

    for i in range(1,altura+1):

        espacios=" "*(altura-i)
        estrellas="*"*(2*i-1)

        arte+=espacios+PASTEL_MENTA+estrellas+RESET+"\n"

    return arte

# =========================================================
# MENU PATRONES
# =========================================================

def menu_patrones():

    limpiar()

    print("1 Triángulo")
    print("2 Cuadrado")
    print("3 Pirámide")

    op=input(COLOR_INPUT+"Elige patrón: "+RESET)

    if op=="1":

        altura=int(input("Altura: "))

        arte=generar_triangulo(altura)

    elif op=="2":

        lado=int(input("Lado: "))

        arte=generar_cuadrado(lado)

    elif op=="3":

        altura=int(input("Altura: "))

        arte=generar_piramide(altura)

    else:
        return

    print("\n"+arte)

    galeria.append(arte)

    input("Enter para continuar")


# =========================================================
# BANNER
# =========================================================

def generar_banner(texto):

    colores = [
        "\033[38;5;219m",
        "\033[38;5;213m",
        "\033[38;5;207m",
        "\033[38;5;201m"
    ]

    ancho = len(texto) + 8

    banner = []

    banner.append("╔" + "═"*ancho + "╗")
    banner.append("║" + " "*ancho + "║")
    banner.append("║   " + texto + " ║")
    banner.append("║" + " "*ancho + "║")
    banner.append("╚" + "═"*ancho + "╝")

    arte=""

    for i,linea in enumerate(banner):

        color = colores[i % len(colores)]

        arte += color + linea + RESET + "\n"

    return arte


def menu_banner():

    limpiar()

    texto = input("Texto del banner: ")

    arte = generar_banner(texto)

    for linea in arte.split("\n"):
        print(linea)
        time.sleep(0.1)

    galeria.append(arte)

    input("Enter para continuar")


# =========================================================
# MARCO
# =========================================================

def generar_marco(texto, estilo):

    ancho = len(texto) + 6

    if estilo == 1:

        top = "✿"*ancho
        side = "❀"

    elif estilo == 2:

        top = "★"*ancho
        side = "✦"

    else:

        top = "♥"*ancho
        side = "♡"

    arte = ""

    arte += top + "\n"
    arte += side + "  " + texto + "  " + side + "\n"
    arte += top + "\n"

    return arte


def menu_marco():

    limpiar()

    texto=input("Texto dentro del marco: ")

    print("1 Floral")
    print("2 Estrellas")
    print("3 Corazones")

    estilo=int(input("Estilo: "))

    arte=generar_marco(texto,estilo)

    print("\n"+arte)

    galeria.append(arte)

    input("Enter para continuar")


# =========================================================
# ANIMACIONES
# =========================================================

def animar_barra_progreso():

    limpiar()

    colores = [
        "\033[31m",
        "\033[33m",
        "\033[32m",
        "\033[36m",
        "\033[35m"
    ]

    for i in range(21):

        color = colores[i % len(colores)]

        barra = color + "■"*i + RESET + "-"*(20-i)

        porcentaje = i*5

        print(f"\r[{barra}] {porcentaje}%",end="")

        time.sleep(0.12)

    print("\n✨ COMPLETO ✨")

    input("Enter")


def animar_texto_movil(texto):

    limpiar()

    for i in range(35):

        limpiar()

        print("\n"*10)

        print(" "*i + texto)

        time.sleep(0.08)

    for i in range(35,0,-1):

        limpiar()

        print("\n"*10)

        print(" "*i + texto)

        time.sleep(0.08)

    input("Enter")


def menu_animaciones():

    limpiar()

    print("1 Barra progreso")
    print("2 Texto móvil")

    op=input("Opción: ")

    if op=="1":

        animar_barra_progreso()

    elif op=="2":

        texto=input("Texto: ")

        animar_texto_movil(texto)

# =========================================================
# MARIPOSA VOLANDO
# =========================================================
def mariposa_lejos():

    frames=[

"""𓂃 ࣪˖ ִֶָ𐀔
𓂃 𓂃 ࣪˖ʚɞ
𓂃𓂃 𓂃 ࣪˖ꕤ""",

"""𓂃𓂃 𓂃 𓂃 ࣪˖ ִֶָ𐀔
𓂃𓂃𓂃𓂃 𓂃 𓂃 ࣪˖ʚɞ
𓂃 𓂃𓂃𓂃𓂃 𓂃𓂃 𓂃 ࣪˖ꕤ"""
]

    for _ in range(6):

        for f in frames:

            limpiar()
            print(PASTEL_AZUL+f+RESET)
            time.sleep(0.5)

def mariposa_grande():

    frames=[

"""
 .;;,
 .,.               .,;;;;;,
;;;;;;;,,        ,;;%%%%%;;
 `;;;%%%%;;,.  ,;;%%;;%%%;;
   `;%%;;%%%;;,;;%%%%%%%;;'
     `;;%%;;%:,;%%%%%;;%%;;,
        `;;%%%,;%%%%%%%%%;;;
           `;:%%%%%%;;%%;;;'
              .:::::::.
                   s.
""",

"""
             ; ,     .;;,
            .;.    .,;;;;;,
            ;;;. ,;;%%%%%;;
            ;;%%,;;%%;;%%%;;
             ;,;;%%%%%%%;;'
             :,;%%%%%;;%%;;,
              ,;%%%%%%%%%;;;
               %%%%%;;%%;;;'
                ::::::.
                   s.
""",

"""
                   ,             ;,
        ;;,           .;;,
        .,.       .,;;;;;,
       ;;;;,,   ,;;%%%%%;;
       %%%%;;,.,;;%%;;%%%;;
       ;;%%%;;,;;%%%%%%%;;'
        %%;;%:,;%%%%%;;%%;;,
        `;;%%%,;%%%%%%%%%;;;
           `;:%%%%%%;;%%;;;'
              .:::::::.
                 s.
"""

]

    for f in frames:

        limpiar()
        print(PASTEL_ROSA+f+RESET)
        time.sleep(0.6)
# =========================================================
# FLOR
# =========================================================
def flor():

    limpiar()

    print(VERDE+r"""              
                     .-~~~-
                .-~~~_._~~~\   
                /~-~~   ~.  `._ 
               /    \     \  | ~~-_ 
       __     |      |     | |  /~\|
   _-~~  ~~-..|       ______||/__..-~~/
    ~-.___     \     /~\_________.-~~
         \~~--._\   |             /
          ^-_    ~\  \          /^
             ^~---|~~~~-.___.-~^
               /~^| | | |^~\
              //~^`/ /_/ ^~\\
              /   //~||      \
                 ~   ||
          ___      -(||      __ ___ _
         |\|  \       ||_.-~~ /|\-  \~-._
         | -\| |      ||/   /  | |\- | |\ \
          \__-\|______ ||  |    \___\|  \_\|
    _____ _.-~/|\     \\||  \  |  /       ~-.
  /'  --/|  / /|  \    \||    \ /          |\~-
 ' ---/| | |   |\  |     ||                 \__|
| --/| | ;  \ /|  /    -(||
`./  |  /     \|/        ||)-
  `~^~^                  ||

"""+RESET)

    time.sleep(2)
# =========================================================
# ZAPATO
# =========================================================

def zapato_cayendo():

    bota=r"""
     .-'\
   .-'  `/\
.-'      `/\
\         `/\
 \         `/\
  \    _-   `/\       _.--.
   \    _-   `/`-..--\     )
    \    _-   `,','  /    ,')
     `-_   -   ` -- ~   ,','
      `-              ,','
       \,--.    ____==-~
        \   \_-~\
         `_-~_.-'
          \-~
"""

    for i in range(12):

        limpiar()
        print("\n"*i)
        print(PASTEL_DURAZNO+bota+RESET)
        time.sleep(0.15)


# =========================================================
# HISTORIA
# =========================================================

def historia_cucaracha():

    limpiar()

    historia = [
        "Una cucaracha solitaria se lamenta y reflexiona...",
        "y se compara con una mariposa.",
        "",
        "Reflexiona...",
        "y piensa que si fuera una mariposa...",
        "todos la querrían..."
    ]

    colores_historia = [
        PASTEL_LILA,
        PASTEL_AZUL,
        PASTEL_MENTA,
        PASTEL_ROSA,
        PASTEL_DURAZNO
    ]

    for linea in historia:

        color = random.choice(colores_historia)

        for letra in linea:
            print(color + letra + RESET, end="", flush=True)
            time.sleep(0.05)

        print()
        time.sleep(1.3)

    time.sleep(2)

    limpiar()
    print(PASTEL_MENTA+"\nUna mariposa aparece a lo lejos...\n"+RESET)
    time.sleep(2)

    mariposa_lejos()

    print(PASTEL_MENTA+"\nLa mariposa se acerca...\n"+RESET)
    time.sleep(2)

    mariposa_grande()

    print(PASTEL_MENTA+"\nLa mariposa llega a una flor...\n"+RESET)
    time.sleep(2)

    flor()

    limpiar()
    print(PASTEL_AMARILLO+"\nAlgo se acerca...\n"+RESET)
    time.sleep(2)

    zapato_cayendo()

    print(ROJO+"\nCRUNCH!!!"+RESET)
    time.sleep(2)

    cucaracha_aplastada()
    
# =========================================================
# CUCARACHA
# =========================================================

def cucaracha_aplastada():

    limpiar()

    print(CAFE+r""",--.       ,---. 
  /    '.    /     \ 
         \  ; 
          \-| 
         (x x)      (/ 
         /'v'     ,-' 
 ,------/ >< \---' 
/)     ;  --  : 
   ,---| ---- |--. 
  ;    | ---- |   : 
 (|  ,-| ---- |-. |) 
    | /| ---- |\ | 
    |/ | ---- | \| 
    \  : ---- ;  | 
     \  \ -- /  / 
     ;   \  /  : 
    /   / \/ \  \ 
   /)           (\
"""+RESET)

    print(ROJO + r"""
    ,--.     .--.
    /    \. ./    \
   /  /\/  "  \/\  \
  / _/ /~~~v~~~\ \_ \
 /    /####|####\    \
;  /\{#####|#####}/\  \
|_/  {#####|#####}  \_:
|    {#####|#####}    |
|   /{#####|#####}\   |
|  / {#####|#####} \  |
| /  {#####|#####}  \ |
|  \ \#####|#####/ /  |
|   \ \####|####/ /   |
 \   \ \###|###/ /   /
  \  /   ~~~~~   \  /
""" + RESET)

    time.sleep(3)

    input(COLOR_INPUT+"\nFin de la historia"+RESET)

# =========================================================
# VER GALERIA
# =========================================================

def ver_galeria():

    limpiar()

    if len(galeria)==0:

        print("Galería vacía")

    else:

        for arte in galeria:

            print(arte)

            print("----------------")

    input("Enter")


# =========================================================
# 🎛 MENU PRINCIPAL
# =========================================================

def menu_principal():

    while True:

        limpiar()

        titulo()

        print()

        print(PASTEL_AZUL+"1"+RESET+" Patrones geométricos")
        print(PASTEL_MENTA+"2"+RESET+" Banner")
        print(PASTEL_LILA+"3"+RESET+" Marcos")
        print(PASTEL_DURAZNO+"4"+RESET+" Animaciones")
        print(PASTEL_AMARILLO+"5"+RESET+" Tabla multiplicar")
        print(PASTEL_ROSA+"6"+RESET+" Tal vez pueda renacer en algo hermoso")
        print(PASTEL_MENTA+"7"+RESET+" Ver galería")
        print(PASTEL_AZUL+"8"+RESET+" Salir")

        op=input(COLOR_INPUT+"\nSeleccione opción: "+RESET)

        if op=="1":
            menu_patrones()

        elif op=="2":
            menu_banner()

        elif op=="3":
            menu_marco()

        elif op=="4":
            menu_animaciones()

        elif op=="5":
            tabla_visual()

        elif op=="6":
            historia_cucaracha()

        elif op=="7":
            ver_galeria()

        elif op=="8":
            break


# =========================================================
# INICIO
# =========================================================

if __name__=="__main__":

    lluvia_inicio()

    menu_principal()