"""1. Escriba un programa donde tendrá los siguientes requisitos (3 ptos):
Reglas:
- Crear una función llamada procesar_notas(estudiantes) la cual va a recibir
un diccionario donde las claves serán los nombres de los estudiantes y sus
valores serán listas con 3 notas.
- Calcular el promedio de cada estudiante.
- Devolver un nuevo diccionario donde la clave sea el nombre del estudiante
y el valor sea otro diccionario con:
promedio: que será el promedio de notas
estado: “aprobado” si es mayor o igual a 11, “desaprobado” si es menor
- Mostrar en pantalla el estudiante con mayor promedio"""

notas_estudiantes = {
    "jOHAN Silva": [13, 12, 18],
    "Juan Arturo": [8, 15, 11],
    "Carlos Juan": [19, 17, 20],
    "Lorena Luna": [5, 10, 7],
    "Mario Robles": [10, 18, 12]
}

def procesar_notas(estudiantes):

    resultados = {}


    for nombre, notas in estudiantes.items():

        promedio = sum(notas) / 3


        if promedio >= 11:
            estado = "aprobado"
        else:
            estado = "desaprobado"

        resultados[nombre] = {
            promedio : estado,
        }

    return resultados

resultados_finales = procesar_notas(notas_estudiantes)


print(" Resultados de los Estudiantes ")
print(resultados_finales)




