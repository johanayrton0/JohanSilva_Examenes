"""3.Crea un programa en Python que implemente una función llamada
convertir_precio(texto: str) -> float que (4 ptos):
1. Reciba un string que representa un precio en soles (ejemplo: "123.50",
"45", "20.99").
2. Intente convertirlo a un número decimal (float).
3. Tenga las siguientes excepciones:
o Si el texto está vacío, debe lanzar un ValueError("El precio no
puede estar vacío").
o Si el texto contiene caracteres inválidos (ejemplo: "abc",

"12a3"), debe lanzar un ValueError("Formato de precio inválido").
o Si el número es negativo, debe lanzar un ValueError("El precio no
puede ser negativo").
- El programa debe pedir tres precios al usuario, usar la función
convertir_precio y almacenarlos en una lista.
- Finalmente, mostrar:
o La lista con los precios convertidos.
o El precio promedio de los tres valores ingresados."""




def convertir_precio(texto: str) -> float:
    if texto == "":
        raise ValueError("El precio no puede estar vacío")
    try:
        precio = float(texto)
    except ValueError:
        raise ValueError("Formato de precio inválido")
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    return precio

precios = []

for i in range(1, 4):
    texto = input(f"Ingrese precio {i}: ")
    try:
        precio = convertir_precio(texto)
        precios.append(precio)
    except ValueError as e:
        print(f"Error: {e}")

precios_validos = [p for p in precios if p >= 0]

print(f"Precios válidos ingresados: {precios_validos}")
if precios_validos:
    promedio = sum(precios_validos) / len(precios_validos)
    print(f"Promedio: {promedio}")
