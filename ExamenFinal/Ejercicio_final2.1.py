import Ejercicio_final2 as ml

print("Caso 1")
lista1 = ml.generar_lista_aleatoria(6)
if lista1:
    no_repetidos1 = ml.obtener_no_repetidos(lista1)
    ml.ordenar_listas(no_repetidos1)
    ml.mayor_par(no_repetidos1)

print(" Caso 2 ")
lista2 = ml.generar_lista_aleatoria(8)
if lista2:
    no_repetidos2 = ml.obtener_no_repetidos(lista2)
    ml.ordenar_listas(no_repetidos2)
    ml.mayor_par(no_repetidos2)
