# Calculadora científica

## MIEMBROS DEL EQUIPO:
ESTHELA NAOMI OROZCO LEAL
MARIANA FABIOLA CISNEROS GARCIA
ELENA YARETZI OCHOA JARILLO
JENNIFER ATHZIRI MARISCAL MAGAÑA

Calculadora con diversas funciones, desde operaciones básicas hasta gráficas integradas
y customizables por cada usuario. El código se divide en los siguientes apartados accesibles 
a través de un menú en loop e interactivo:

1. Calculadora básica. 
Como su nombre lo dice, esta función te permite realizar operaciones básicas como suma, resta 
divisón, multiplicación, potencia y módulos. 

2. Conversor de Unidades
Convierte unidades de medida de:
    KB → Bytes
    KB → MB
    MB → KB
    MB → GB
    GB → MB

3. Sistemas Numéricos
En este apartado el usuario podrá convertir de un sistema numérico con facilidad:
    Decimal → Binario
    Decimal → Hexadecimal
    Binario → Decimal
    Hexadecimal → Decimal

4. Estadísticas
Con base en los datos ingresados por el usuario, el sistema permite crear una comparativa
y da como resultado el promedio.

5. Gráfico ASCII de frecuencia
A partir de la lectura del def inicial, hace un llamado a las demás funciones para que la  
calculadora lleve a cabo un gráfico.

6. Ver Historial
Se almacenan las operaciones realizadas en caso de que el usuario necesite consultarlas de nuevo.

7. Historial a CSV
Convierte las operaciones ingresadas por el usuario a un archivo CSV, el cual nos permite tener
una versión del archivo tipo texto.

8. Análisis con Pandas
Los datos almacenados pueden modificarse con las funciones panda, arrojando una lista de resultados
usando esta función.

9. Comparación de usuarios
Es posible comparar el tiempo de uso realizado por los usuarios.

10. Generar gráfico JPG
En base a las operaciones es posible generar un gráfico en formato JPG.

11. Modo Batch
El programa abre un archivo para realizar varias operaciones al mismo tiempo.

12. Salir
Rompe el loop y se cierra la calculadora.


El programa permite crear más de un usuario e intercambiar entre los mmismos, además de 
generar un formato json y guardar los resultados en archivos csv y gráficos PNG de todas 
las operaciones realizadas. Es importante mencionar que cuenta con el historial de las 
operaciones realizadas en caso de que el usuario necesite recurrir a ver las operaciones 
hechas con anterioridad. 

## Instrucciones de uso

1. Abre tu terminal: * En Windows: Presiona la tecla Win, escribe cmd o PowerShell y pulsa Enter. Para Mac o Linux abre el apartado terminal que se muestra en la parte superior izquirda de tu pantalla.
2. Navega a la carpeta del proyecto: Usa el comando cd seguido de la ruta donde guardaste los archivos.(Ejemplo:cd Documents/ProyectoCalculadora)
3. Instala las librerías necesarias: Para que los gráficos y el análisis de datos funcionen, escribe el siguiente comando y pulsa Enter: pip install pandas matplotlib
4. Inicia la calculadora: Escribe el siguiente comando en la terminal: python calculadora.py
5. Al iniciar, la terminal te mostrará el mensaje: Ingrese su nombre de usuario:.
6. Escribe tu nombre (o un alias) y presiona Enter.
7. El sistema te dará la bienvenida en color verde: ¡Bienvenida [Nombre]!.
8. Verás una lista numerada del 1 al 12. Escribe el número de la sección que deseas (ejemplo: 1 para Calculadora Básica) y presiona Enter.
9. Si entraste a una calculadora, aparecerá otro menú (Suma, Resta, etc.). Escribe el número de la operación y presiona Enter.
10. La terminal te pedirá: Ingrese el primer número:. Escríbelo y presiona Enter.
11. Luego te pedirá: Ingrese el segundo número:. Escríbelo y presiona Enter.
12. El resultado aparecerá resaltado en verde. Automáticamente, esta operación se guardará en tu historial personal.
13. Ver estadísticas (Opción 4): El sistema analizará tus resultados y te dirá cuál fue el número más alto, el más bajo y el promedio de tus cálculos.
14. Gráfico ASCII (Opción 5): Generará una gráfica visual directamente en la terminal usando caracteres de texto para mostrar qué operaciones usas más.
15.  Ver historial (Opción 6): Muestra cuantas operaciones se han hecho por usuario y quien lo ha utilizado más frecuentemente. Dentro de la misma terminal aparece el historial realizado en ese momento(al utilizar la calculadora)
16. Guardar en Excel/CSV (Opción 7):Los datos los tiene tabulados. Este archivo lo puedes abrir con Excel como una de las opciones.
17. Opción 8 (Análisis con Pandas): El programa usará herramientas de ciencia de datos para mostrarte un resumen técnico de quién es el usuario más activo y qué tipo de cálculos predominan en el sistema.
18. Opción 9 (Modo Batch): Permite que la calculadora lea un archivo externo y realice múltiples operaciones automáticamente sin que tú tengas que teclear nada.
19. Generar imagen JPG (Opción 10): Al seleccionar esto, el programa creará una gráfica de barras profesional llamada grafico_operaciones.jpg.
20. Cerrar el programa (Opción 12): No cierres la ventana de la terminal directamente. Selecciona la opción 12 y presiona Enter.
21. Esto activará el guardado automático en el archivo historial.json, asegurando que cuando vuelvas a abrir la calculadora, tus datos sigan ahí.
22. Verás el mensaje de despedida: Guardando historial... Byes <3

Esperamos este manual de uso te sea útil y haga tu experiencia de navegación por la calculadora mucho más sencilla.