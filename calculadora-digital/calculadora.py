"""
Proyecto 1: Calculadora 
Carrera: Creatividad Digital
Equipo: 
Elena Yaretzi Ochoa Jarillo
Mariana Fabiola Cisneros García 
Jennifer Atzhiri Mariscal Ocampo 
Esthela Naomi Orozco Leal 

"""

import os
from datetime import datetime
import csv
import json
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import math

# ==============================
# COLORSITOS
# ==============================

class Colores:
    HEADER = "\033[95m"
    AZUL = "\033[94m"
    VERDE = "\033[92m"
    AMARILLO = "\033[93m"
    ROJO = "\033[91m"
    FIN = "\033[0m"

# ==============================
# VARIABLES GLOBALES
# ==============================

HISTORIAL = []
RUTA_HISTORIAL = "datos/historial.json"

# ==============================
# SISTEMA DE USUARIOS
# ==============================

USUARIO_ACTUAL = None

# ==============================
# UTILIDADES GENERALES
# ==============================

def validar_numero(mensaje):
    """
    Valida que el usuario ingrese un número.
    """
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print(f"{Colores.ROJO}Error: Ingrese un número válido.{Colores.FIN}")

def guardar_historial():
    """
    Guarda el historial en archivo en formato JSON.
    Se usa JSON porque ahora guardamos diccionarios,
    no texto plano.
    """
    os.makedirs("datos", exist_ok=True)

    with open(RUTA_HISTORIAL, "w", encoding="utf-8") as archivo:
        json.dump(HISTORIAL, archivo, indent=4)

def cargar_historial():
    """
    Carga el historial si existe.
    """
    if os.path.exists(RUTA_HISTORIAL):
        with open(RUTA_HISTORIAL, "r", encoding="utf-8") as archivo:
            try:
                datos = json.load(archivo)
                HISTORIAL.extend(datos)
            except:
                pass  # Si el archivo está vacío o corrupto, no rompe el programa
def login():
    """
    Permite registrar o ingresar usuario.
    """
    global USUARIO_ACTUAL

    usuario = input("Ingrese su nombre de usuario: ")

    if not usuario.strip():
        print(f"{Colores.ROJO}Usuario inválido.{Colores.FIN}")
        return login()

    USUARIO_ACTUAL = usuario
    print(f"{Colores.VERDE}Bienvenida {usuario}!{Colores.FIN}")

def agregar_historial(operacion, num1, num2, resultado):
    """
    Agrega una operación al historial pues en un formato mas estructurado, agregamos diccionarios aqui.
    """
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    registro = {
        "usuario": USUARIO_ACTUAL,
        "fecha": fecha,
        "operacion": operacion,
        "num1": num1,
        "num2": num2,
        "resultado": resultado
    }

    HISTORIAL.append(registro)
  # Limite del historial
    if len(HISTORIAL) > 10:
        HISTORIAL.pop(0)

def mostrar_historial():
    """
    Muestra el historial formateado de manera bonita.
    """
    if not HISTORIAL:
        print("No hay operaciones registradas.")
        return

    print(f"{Colores.AZUL}--- HISTORIAL ---{Colores.FIN}")
    for registro in HISTORIAL:
        if registro["num2"] is not None:
            print(f"{registro['fecha']} | {registro['num1']} {registro['operacion']} {registro['num2']} = {registro['resultado']}")
        else:
            print(f"{registro['fecha']} | {registro['operacion']} | {registro['num1']} → {registro['resultado']}")

# ==============================
# CALCULADORA BÁSICA
# ==============================

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        print(f"{Colores.ROJO}Error: No se puede dividir entre cero.{Colores.FIN}")
        return None
    return a / b

def modulo(a, b):
    return a % b

def potencia(a, b):
    return a ** b

OPERACIONES = {
    "1": ("Suma", lambda a, b: a + b, "+"),
    "2": ("Resta", lambda a, b: a - b, "-"),
    "3": ("Multiplicación", lambda a, b: a * b, "*"),
    "4": ("División", dividir, "/"),
    "5": ("Módulo", lambda a, b: a % b, "%"),
    "6": ("Potencia", lambda a, b: a ** b, "^"),
    "7": ("Factorial", lambda a, b: math.factorial(int(a)), "!"),
    "8": ("Raíz Cuadrada", lambda a, b: math.sqrt(a), "√"),
}

CONVERSIONES = {
    "1": ("Bytes → KB", lambda x: x / 1024, "Bytes", "KB"),
    "2": ("KB → Bytes", lambda x: x * 1024, "KB", "Bytes"),
    "3": ("KB → MB", lambda x: x / 1024, "KB", "MB"),
    "4": ("MB → KB", lambda x: x * 1024, "MB", "KB"),
    "5": ("MB → GB", lambda x: x / 1024, "MB", "GB"),
    "6": ("GB → MB", lambda x: x * 1024, "GB", "MB"),
}

def menu_calculadora_basica():
    while True:
        print(f"{Colores.AZUL}--- CALCULADORA BÁSICA ---{Colores.FIN}")

        for clave, valor in OPERACIONES.items():
            print(f"{clave}. {valor[0]}")
        print("9. Volver")

        opcion = input(f"{Colores.AMARILLO}Seleccione una opción: {Colores.FIN}")

        if opcion == "9":
            break

        if opcion not in OPERACIONES:
            print(f"{Colores.ROJO}Opción inválida.{Colores.FIN}")
            continue

        a = validar_numero("Ingrese el primer número: ")
        b = validar_numero("Ingrese el segundo número: ")

        nombre, funcion, simbolo = OPERACIONES[opcion]
        resultado = funcion(a, b)

        if resultado is None:
            continue

        operacion = f"{a} {simbolo} {b} = {resultado}"
        print(f"Resultado: {Colores.VERDE}{operacion}{Colores.FIN}")
        agregar_historial(simbolo, a, b, resultado)
# ==============================
# CONVERSOR DE UNIDADES
# ==============================

def bytes_a_kb(bytes_):
    return bytes_ / 1024

def kb_a_bytes(kb):
    return kb * 1024

def kb_a_mb(kb):
    return kb / 1024

def mb_a_kb(mb):
    return mb * 1024

def mb_a_gb(mb):
    return mb / 1024

def gb_a_mb(gb):
    return gb * 1024

def menu_conversor_unidades():
    while True:
        print(f"{Colores.AZUL}--- CONVERSOR DE UNIDADES ---{Colores.FIN}")

        for clave, valor in CONVERSIONES.items():
            print(f"{clave}. {valor[0]}")
        print("7. Volver")

        opcion = input(f"{Colores.AMARILLO}Seleccione una opción: {Colores.FIN}")

        if opcion == "7":
            break

        if opcion not in CONVERSIONES:
            print(f"{Colores.ROJO}Opción inválida.{Colores.FIN}")
            continue
        valor = validar_numero("Ingrese el valor: ")

        nombre, funcion, unidad_origen, unidad_destino = CONVERSIONES[opcion]
        resultado = funcion(valor)

        operacion = f"{valor} {unidad_origen} → {resultado} {unidad_destino}"
        print(f"Resultado: {Colores.VERDE}{operacion}{Colores.FIN}")
        agregar_historial(nombre, valor, None, resultado)

# ==============================
# SISTEMAS NUMÉRICOS
# ==============================

def decimal_a_binario(numero):
    """
    Convierte decimal a binario manualmente.
    """
    numero = int(numero)
    if numero == 0:
        return "0"

    binario = ""
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2

    return binario


def decimal_a_hexadecimal(numero):
    return hex(int(numero))[2:].upper()


def binario_a_decimal(numero):
    return int(numero, 2)


def hexadecimal_a_decimal(numero):
    return int(numero, 16)

SISTEMAS = {
    "1": ("Decimal → Binario", decimal_a_binario),
    "2": ("Decimal → Hexadecimal", decimal_a_hexadecimal),
    "3": ("Binario → Decimal", binario_a_decimal),
    "4": ("Hexadecimal → Decimal", hexadecimal_a_decimal),
}

def menu_sistemas_numericos():
    while True:
        print(f"{Colores.AZUL}--- SISTEMAS NUMÉRICOS ---{Colores.FIN}")

        for clave, valor in SISTEMAS.items():
            print(f"{clave}. {valor[0]}")
        print("5. Volver")

        opcion = input(f"{Colores.AMARILLO}Seleccione una opción: {Colores.FIN}")

        if opcion == "5":
            break

        if opcion not in SISTEMAS:
            print(f"{Colores.ROJO}Opción inválida.{Colores.FIN}")
            continue

        numero = input("Ingrese el número: ")

        try:
            nombre, funcion = SISTEMAS[opcion]
            resultado = funcion(numero)

            operacion = f"{nombre}: {numero} → {resultado}"
            print(f"Resultado: {Colores.VERDE}{operacion}{Colores.FIN}")
            agregar_historial(nombre, numero, None, resultado)

        except ValueError:
            print(f"{Colores.ROJO}Error: Número inválido para esa conversión.{Colores.FIN}")

# ==============================
# Estadísticas del historial
# ==============================

def estadisticas_historial():
    if not HISTORIAL:
        print(f"{Colores.ROJO}No hay datos para analizar.{Colores.FIN}")
        return

    print(f"{Colores.AZUL}--- ESTADÍSTICAS CON PANDAS ---{Colores.FIN}")

    # Convertimos el historial (lista de diccionarios) a DataFrame
    df = pd.DataFrame(HISTORIAL)

    print(f"Total de operaciones: {len(df)}")

    # Solo analizamos resultados numéricos
    df_numericos = df[pd.to_numeric(df["resultado"], errors="coerce").notnull()]

    if not df_numericos.empty:
        promedio = df_numericos["resultado"].mean()
        maximo = df_numericos["resultado"].max()
        minimo = df_numericos["resultado"].min()

        print(f"{Colores.VERDE}Promedio: {round(promedio,2)}{Colores.FIN}")
        print(f"{Colores.VERDE}Máximo: {maximo}{Colores.FIN}")
        print(f"{Colores.VERDE}Mínimo: {minimo}{Colores.FIN}")
    else:
        print("No hay resultados numéricos para analizar.")

def generar_grafica():
    if not HISTORIAL:
        print(f"{Colores.ROJO}No hay datos para graficar.{Colores.FIN}")
        return

    df = pd.DataFrame(HISTORIAL)

    df["resultado"].plot(kind="line")
    plt.title("Resultados del Historial")
    plt.xlabel("Operaciones")
    plt.ylabel("Resultado")

    plt.show()
# -------------------------
# GRÁFICO ASCII DE FRECUENCIA
# -------------------------
def grafico_frecuencia():
    if not HISTORIAL:
        print(f"{Colores.AZUL}No hay datos.{Colores.FIN}")
        return

    conteo = {}

    for registro in HISTORIAL:
        operacion = registro["operacion"]
        conteo[operacion] = conteo.get(operacion, 0) + 1

    print(f"\n{Colores.AZUL}--- FRECUENCIA DE OPERACIONES ---{Colores.FIN}")

    for clave, valor in conteo.items():
        print(f"{Colores.VERDE}{clave}: {'█' * valor} ({valor}){Colores.FIN}")

# -------------------------
# PS EL CSV
# -------------------------
def exportar_csv():
    """
    Exporta el historial (formato diccionario) a CSV, inluyendo usuario.
    """
    if not HISTORIAL:
        print(f"{Colores.ROJO}No hay datos para exportar.{Colores.FIN}")
        return

    with open("datos/historial.csv", "w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)

        # Encabezados
        writer.writerow(["Usuario", "Fecha", "Operacion", "Num1", "Num2", "Resultado"])

        # Escribir cada registro del historial
        for registro in HISTORIAL:
            writer.writerow([
                registro["usuario"],
                registro["fecha"],
                registro["operacion"],
                registro["num1"],
                registro["num2"],
                registro["resultado"]
            ])

    print(f"{Colores.VERDE}Historial exportado correctamente a datos/historial.csv{Colores.FIN}")

# ==============================
# ANÁLISIS CON PANDAS
# ==============================

def analisis_con_pandas():
    """
    Analiza el historial usado pandas.
    """

    if not HISTORIAL:
        print(f"{Colores.ROJO}No hay datos para analizar.{Colores.FIN}")
        return

    df = pd.DataFrame(HISTORIAL)

    print(f"{Colores.AZUL}--- ANÁLISIS CON PANDAS ---{Colores.FIN}")

    print("\nOperaciones por usuario:")
    print(df["usuario"].value_counts())

    print("\nOperaciones más usadas:")
    print(df["operacion"].value_counts())

    # Solo resultados numéricos
    df_numericos = df[pd.to_numeric(df["resultado"], errors="coerce").notnull()]
    df_numericos["resultado"] = df_numericos["resultado"].astype(float)

    if not df_numericos.empty:
        print("\nEstadísticas de resultados:")
        print(df_numericos["resultado"].describe())

# ==============================
# COMPARACIÓN ENTRE USUARIOS
# ==============================

def comparar_usuarios():
    if not HISTORIAL:
        print(f"{Colores.ROJO}No hay datos.{Colores.FIN}")
        return

    df = pd.DataFrame(HISTORIAL)

    print(f"{Colores.AZUL}--- COMPARACIÓN DE USUARIOS ---{Colores.FIN}")

    conteo = df["usuario"].value_counts()

    for usuario, cantidad in conteo.items():
        print(f"{Colores.VERDE}{usuario}: {cantidad} operaciones{Colores.FIN}")

    usuario_top = conteo.idxmax()
    print(f"\nUsuario más activo: {Colores.AMARILLO}{usuario_top}{Colores.FIN}")

# ==============================
# GRÁFICO REAL EN JPG
# ==============================

def generar_grafico_jpg():
    if not HISTORIAL:
        print(f"{Colores.ROJO}No hay datos.{Colores.FIN}")
        return

    df = pd.DataFrame(HISTORIAL)

    conteo = df["operacion"].value_counts()

    plt.figure()
    conteo.plot(kind="bar")
    plt.title("Frecuencia de Operaciones")
    plt.xlabel("Operacion")
    plt.ylabel("Cantidad")

    plt.savefig("datos/grafico_operaciones.jpg")
    plt.close()

    print(f"{Colores.VERDE}Gráfico guardado en datos/grafico_operaciones.jpg{Colores.FIN}")

# ==============================
# MUD BATCH
# ==============================

def modo_batch():
    """
    Ejecuta operaciones desde un archivo operaciones.txt
    Formato esperado:
    2 + 3
    5 * 8
    7 !
    16 √
    """

    try:
        ruta_base = os.path.dirname(__file__)
        ruta_archivo = os.path.join(ruta_base, "operaciones.txt")

        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            print(f"{Colores.AZUL}--- MODO BATCH ACTIVADO ---{Colores.FIN}")

            for linea in archivo:
                linea = linea.strip()

                if not linea:
                    continue

                print(f"\nProcesando: {Colores.AMARILLO}{linea}{Colores.FIN}")

                partes = linea.split()

                try:
                    # Operaciones binarias (2 + 3)
                    if len(partes) == 3:
                        a = float(partes[0])
                        operador = partes[1]
                        b = float(partes[2])

                        if operador == "+":
                            resultado = sumar(a, b)
                        elif operador == "-":
                            resultado = restar(a, b)
                        elif operador == "*":
                            resultado = multiplicar(a, b)
                        elif operador == "/":
                            resultado = dividir(a, b)
                        elif operador == "%":
                            resultado = modulo(a, b)
                        elif operador == "^":
                            resultado = potencia(a, b)
                        else:
                            print(f"{Colores.ROJO}Operador inválido.{Colores.FIN}")
                            continue

                        print(f"Resultado: {Colores.VERDE}{resultado}{Colores.FIN}")
                        agregar_historial(operador, a, b, resultado)

                    # Operaciones unarias (5 !  o 16 √)
                    elif len(partes) == 2:
                        a = float(partes[0])
                        operador = partes[1]

                        if operador == "!":
                            resultado = math.factorial(int(a))
                        elif operador == "√":
                            resultado = math.sqrt(a)
                        else:
                            print(f"{Colores.ROJO}Operador inválido.{Colores.FIN}")
                            continue

                        print(f"Resultado: {Colores.VERDE}{resultado}{Colores.FIN}")
                        agregar_historial(operador, a, None, resultado)

                    else:
                        print(f"{Colores.ROJO}Formato incorrecto en línea: {linea}{Colores.FIN}")

                except Exception as e:
                    print(f"{Colores.ROJO}Error procesando línea: {linea}{Colores.FIN}")

    except FileNotFoundError:
        print(f"{Colores.ROJO}Archivo operaciones.txt no encontrado en la carpeta del proyecto.{Colores.FIN}")

# ==============================
# MENÚ PRINCIPAL
# ==============================

def menu_principal():
    cargar_historial()
    login()

    while True:
        print(Colores.HEADER + "="*50)
        print(" CALCULADORA DIGITAL")
        print("="*50 + Colores.FIN)
        print("1. Calculadora Básica")
        print("2. Conversor de Unidades")
        print("3. Sistemas Numéricos")
        print("4. Estadísticas")
        print("5. Gráfico ASCII de frecuencia")
        print("6. Ver Historial")
        print("7. Historial a CSV")
        print("8. Análisis con Pandas")
        print("9. Comparación de usuarios")
        print("10. Generar gráfico JPG")
        print("11. Modo Batch")
        print("12. Salir")

        opcion = input(f"{Colores.AMARILLO}Seleccione una opción: {Colores.FIN}")

        if opcion == "1":
            menu_calculadora_basica()
        elif opcion == "2":
            menu_conversor_unidades()
        elif opcion == "3":
            menu_sistemas_numericos()
        elif opcion == "4":
            estadisticas_historial()
        elif opcion == "5":
            grafico_frecuencia()
        elif opcion == "6":
            mostrar_historial()
        elif opcion == "7":
            exportar_csv()
        elif opcion == "8":
            analisis_con_pandas()
        elif opcion == "9":
            comparar_usuarios()
        elif opcion == "10":
            generar_grafico_jpg()
        elif opcion == "11":
            modo_batch() 
        elif opcion == "12":
            guardar_historial()
            print("Guardando historial... Byes<3")
            break
        else:
            print(f"{Colores.ROJO}Opción inválida.{Colores.FIN}")

if __name__ == "__main__":
    menu_principal()