"""
Proyecto: Sistema de Resumen Estadístico
Hecho Por: Mariana Fabiola Cisneros Garcia

Descripción:
Sistema interactivo que analiza calificaciones académicas
y temperaturas semanales utilizando estadística descriptiva.
Incluye validación de datos, visualización en consola y
generación automática de reportes.
"""

import csv
import statistics
import os


# ==================================================
# UTILIDADES GENERALES
# ==================================================

def imprimir_titulo(texto):
    print("\n" + "=" * 70)
    print(texto.center(70))
    print("=" * 70)


def grafico_barras(etiquetas, valores, ancho_max=40):
    if not valores:
        return

    max_val = max(valores)
    print("\n")

    for etiqueta, valor in zip(etiquetas, valores):
        longitud = int((valor / max_val) * ancho_max) if max_val != 0 else 0
        barra = "█" * longitud
        print(f"{etiqueta:15} | {barra} {valor:.2f}")


def asegurar_carpeta_Reportes_0_0():
    if not os.path.exists("Reportes_0_0"):
        os.makedirs("Reportes_0_0")


# ==================================================
#  ANALIZADOR DE CALIFICACIONES
# ==================================================

class AnalizadorCalificaciones:

    def __init__(self, archivo):
        self.archivo = archivo
        self.estudiantes = self.cargar_datos()

    def cargar_datos(self):
        estudiantes = []

        if not os.path.exists(self.archivo):
            print("⚠ ERROR: El archivo CSV no existe.")
            return estudiantes

        with open(self.archivo, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                estudiantes.append({
                    "nombre": fila["nombre"],
                    "matematicas": float(fila["matematicas"]),
                    "fisica": float(fila["fisica"]),
                    "quimica": float(fila["quimica"]),
                    "historia": float(fila["historia"])
                })
        return estudiantes

    def ejecutar(self):
        if not self.estudiantes:
            print("No hay datos para analizar.")
            return

        imprimir_titulo("ANÁLISIS DE CALIFICACIONES")

        materias = ["matematicas", "fisica", "quimica", "historia"]
        promedios_materias = {}

        for e in self.estudiantes:
            promedio = sum(e[m] for m in materias) / len(materias)
            print(f"{e['nombre']:15} → Promedio: {promedio:.2f}")

        print("\nESTADÍSTICAS POR MATERIA")

        for materia in materias:
            datos = [e[materia] for e in self.estudiantes]

            media = statistics.mean(datos)
            mediana = statistics.median(datos)
            desviacion = statistics.stdev(datos) if len(datos) > 1 else 0

            promedios_materias[materia] = media

            print(f"\n{materia.upper()}")
            print(f"Media: {media:.2f}")
            print(f"Mediana: {mediana:.2f}")
            print(f"Desviación estándar: {desviacion:.2f}")

        materia_facil = max(promedios_materias, key=promedios_materias.get)
        materia_dificil = min(promedios_materias, key=promedios_materias.get)

        print(f"\nMateria más fácil: {materia_facil}")
        print(f"Materia más difícil: {materia_dificil}")

        grafico_barras(
            list(promedios_materias.keys()),
            list(promedios_materias.values())
        )

        self.generar_reporte(promedios_materias)

    def generar_reporte(self, promedios_materias):
        asegurar_carpeta_Reportes_0_0()
        ruta = "Reportes_0_0/reporte_calificaciones.txt"

        with open(ruta, "w", encoding="utf-8") as f:
            f.write("REPORTE DE CALIFICACIONES\n\n")
            for materia, promedio in promedios_materias.items():
                f.write(f"{materia}: {promedio:.2f}\n")

        print(f"\nReporte generado en: {ruta}")


# ==================================================
# ANALIZADOR DE TEMPERATURAS
# ==================================================

class AnalizadorTemperaturas:

    def solicitar_datos(self):
        dias = ["Lunes", "Martes", "Miércoles",
                "Jueves", "Viernes", "Sábado", "Domingo"]
        temperaturas = []

        imprimir_titulo("ANÁLISIS DE TEMPERATURAS")

        for dia in dias:
            while True:
                try:
                    temp = float(input(f"{dia}: "))
                    temperaturas.append(temp)
                    break
                except ValueError:
                    print("Ingrese un número válido.")

        return dias, temperaturas

    def ejecutar(self):
        dias, temperaturas = self.solicitar_datos()

        media = statistics.mean(temperaturas)
        mediana = statistics.median(temperaturas)
        desviacion = statistics.stdev(temperaturas) if len(temperaturas) > 1 else 0

        print("\nRESULTADOS")
        print(f"Media: {media:.2f}")
        print(f"Mediana: {mediana:.2f}")
        print(f"Desviación estándar: {desviacion:.2f}")

        print("\nDÍAS EXTREMOS (±2 desviaciones)")
        for dia, temp in zip(dias, temperaturas):
            if desviacion > 0 and abs(temp - media) > 2 * desviacion:
                print(f"{dia}: {temp:.2f}°C")

        grafico_barras(dias, temperaturas)

        self.generar_reporte(dias, temperaturas)

    def generar_reporte(self, dias, temperaturas):
        asegurar_carpeta_Reportes_0_0()
        ruta = "Reportes_0_0/reporte_temperaturas.txt"

        with open(ruta, "w", encoding="utf-8") as f:
            f.write("REPORTE DE TEMPERATURAS\n\n")
            for dia, temp in zip(dias, temperaturas):
                f.write(f"{dia}: {temp:.2f}°C\n")

        print(f"\nReporte generado en: {ruta}")


# ==================================================
# MENÚ PRINCIPAL
# ==================================================

def menu():
    while True:
        imprimir_titulo("SISTEMA DE RESUMEN ESTADÍSTICO")

        print("1. Analizar Calificaciones")
        print("2. Analizar Temperaturas")
        print("3. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            analizador = AnalizadorCalificaciones("calificacionesYe.csv")
            analizador.ejecutar()
            input("\nPresione Enter para continuar...")
        elif opcion == "2":
            analizador = AnalizadorTemperaturas()
            analizador.ejecutar()
            input("\nPresione Enter para continuar...")
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")


# ==================================================
# EJECUCIÓN PRINCIPAL
# ==================================================

if __name__ == "__main__":
    menu()