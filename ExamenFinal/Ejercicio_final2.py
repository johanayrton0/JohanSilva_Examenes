"""- Crear una función que le permitirá almacenar X números aleatorios en
una lista y finalmente los imprimirá por consola al llamar la función. X
solo puede ser entero. No otro tipo de dato. Y también un índice
existente en la lista (usar para esto excepciones)
- Crear una función que le permita almacenar los números no repetidos de
la lista anterior, la función retornará este valor para que pueda ser
impreso por consola.
- Crear una función donde se creará una lista para ordenar de mayor a
menor la lista que se creó en el ítem anterior (número no repetidos) y
otra lista para ordenarlas de menor a mayor, retornar este valor e
imprimirlos por consola.
- Crear una función para indicar cuál es el mayor número par de la lista
(lista de la regla 2), retornar este valor e imprimirlo por consola.
- Crear el archivo main.py, donde solo llamarás las anteriores funciones que
se encontrarán alojadas en un módulo (probarlo para dos casos mínimo)"""


import random
def generar_lista_aleatoria(x):
    try:
        if not isinstance(x, int):
            raise TypeError("El valor de X debe ser un número entero.")
        lista = [random.randint(1, 100) for _ in range(x)]
        print(f"Lista generada ({x} elementos): {lista}")


        indice = int(input(f"Ingrese un índice entre 0 y {len(lista)-1}: "))
        try:
            print(f"Elemento en el índice {indice}: {lista[indice]}")
        except IndexError:
            print(" Error: El índice no existe en la lista.")

        return lista

    except TypeError as e:
        print(f" Error: {e}")
    except ValueError:
        print(" Error: Debe ingresar un número entero para el índice.")

def obtener_no_repetidos(lista):
    lista_sin_repetidos = list(set(lista))
    print(f"Números no repetidos: {lista_sin_repetidos}")
    return lista_sin_repetidos

def ordenar_listas(lista):
    mayor_a_menor = sorted(lista,
                           reverse=True)
    menor_a_mayor = sorted(lista)
    print(f"Orden descendente: {mayor_a_menor}")
    print(f"Orden ascendente: {menor_a_mayor}")
    return mayor_a_menor, menor_a_mayor

def mayor_par(lista):
    pares = [n for n in lista if n % 2 == 0]
    if pares:
        max_par = max(pares)
        print(f"El mayor número par es: {max_par}")
        return max_par
    else:
        print(" No hay números pares en la lista.")
        return None
