"""2. Usando el concepto de funciones (3 ptos):
Reglas:
- Crear una función normalizar_nombres(nombres)
- El parámetro recibe una lista de string de nombres (6 como mínimo)
- Este quitará el espacio antes y después si lo hubiera
- Convierte en tipo título
- Si hubiera más nombre los debe separar (si debe haber el caso en el input de
datos)
- Devuelve también eliminando duplicados manteniendo el orden de la primera
- No mutará la lista original"""


def normalizar_nombres(nombres: list) -> list:

    nombres_limpios = []

    vistos = set()

    for nombre_sucio in nombres:

        nombre_limpio = nombre_sucio.strip()

        if ',' in nombre_limpio:
            sub_nombres = [n.strip() for n in nombre_limpio.split(',')]
        else:
            sub_nombres = [nombre_limpio]

        for nombre in sub_nombres:

            if not nombre:
                continue

            nombre_titulo = nombre.title()

            if nombre_titulo not in vistos:
                nombres_limpios.append(nombre_titulo)
                vistos.add(nombre_titulo)

    return nombres_limpios

nombres_originales = [
    "  pablo lopez  ",
    "ANA rodriguez",
    "maria garcia",
    "  pablo lopez  ",
    "Luis Perez ",
    "MARIA garcia",
    "pedro,juan,luis",
    "Elias"
]
print(f"Lista original:\n{nombres_originales}")

nombres_normalizados = normalizar_nombres(nombres_originales)

print("\n" + "=" * 40 + "\n")
print(f"Lista de nombres normalizados y sin duplicados:\n{nombres_normalizados}")

print(f"\nLista original después de la función (debe ser la misma):\n{nombres_originales}")