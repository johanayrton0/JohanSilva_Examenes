import time


def medir_tiempo(funcion):

    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f" La función '{funcion.__name__}' tardó {fin - inicio:.6f} segundos.")
        return resultado

    return wrapper

class Persona:

    def __init__(self, nombre, edad, ciudad):
        if not isinstance(nombre, str):
            raise TypeError(" Debe ser de tipo string ")
        self.__nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    @property
    def nombre(self):
        return self.__nombre

    @medir_tiempo
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nCiudad: {self.ciudad}")

class Empleado(Persona):

    def __init__(self, nombre, edad, ciudad, sueldo):
        super().__init__(nombre, edad, ciudad)
        self.sueldo = sueldo

    @medir_tiempo
    def impuesto(self):
        if self.sueldo > 5500:
            impuesto_a_pagar = self.sueldo * 0.09
            print(f" El empleado debe pagar impuestos.")
            return impuesto_a_pagar
        else:
            print(" El empleado no requiere pagar impuestos.")
            return 0.0

    def mostrar_datos_completos(self):
        super().mostrar_datos()
        print(f"Sueldo: {self.sueldo:.2f} soles")


registro_empleados = []


@medir_tiempo
def manejoDiccionario(empleado):
    print("\nProcesando y agregando empleado al registro...")
    try:
        impuesto_calculado = empleado.impuesto()

        datos_empleado = {
            "nombre": empleado.nombre,
            "edad": empleado.edad,
            "sueldo": empleado.sueldo,
            "impuesto": impuesto_calculado
        }

        registro_empleados.append(datos_empleado)
        print("Empleado agregado al diccionario de registros.")

    except Exception as e:
        print(f" Ocurrió un error al agregar al empleado: {e}")

@medir_tiempo
def encontrar_empleado(nombre_buscado, registro):

    encontrado = False
    for empleado in registro:
        if empleado["nombre"].lower() == nombre_buscado.lower():
            print("\n Empleado Encontrado ")
            print(
                f"El empleado {empleado['nombre']} tiene una remuneración de {empleado['sueldo']:.2f} y un impuesto de {empleado['impuesto']:.2f}")
            encontrado = True
            break
    if not encontrado:
        print(f"\n No se encontró un empleado con el nombre {nombre_buscado} ")

if __name__ == "__main__":
    while True:
        print("\n Ingrese los datos del nuevo empleada ")
        try:
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            ciudad = input("Ciudad: ")
            sueldo = float(input("Sueldo (soles): "))

            emp = Empleado(nombre, edad, ciudad, sueldo)

            print("\n Datos del Empleado ")
            emp.mostrar_datos_completos()

            manejoDiccionario(emp)

        except (ValueError, TypeError) as e:
            print(f"Error en el ingreso de datos: {e}. Por favor, intente de nuevo.")

        continuar = input("\n¿Agregar otro empleado? (s/n): ").lower()
        if continuar != 's':
            break

    if registro_empleados:
        print("\nBúsqueda de Empleados ")
        nombre_a_buscar = input("Ingrese el nombre del empleado a buscar: ")
        encontrar_empleado(nombre_a_buscar, registro_empleados)
