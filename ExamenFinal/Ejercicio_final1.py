"""Clase base Persona
o Atributos: nombre, edad, nacionalidad="peruana", saldo=0.0.
o Métodos para esta clase:
▪ actualizar_nombre(nombre) y actualizar_edad(edad)
(validar edad > 0).
▪ cumplir_anios() (incrementa edad en 1).
▪ mostrar_saldo() (imprime el saldo actual).
▪ transferir(destino, monto) (si no hay fondos
suficientes, imprimir “Saldo insuficiente”; si hay,
basarse en self y acreditar a destino).
• Crear la clase que hereda: Empleado(Persona)
o Atributo adicional: sueldo (float).
o Métodos para esta clase:
▪ aumento_sueldo(porcentaje=0.30) (incrementa el
sueldo en 30% por defecto).
▪ prediccion(anio_objetivo, edad_param=None)
▪ Retorna el mensaje: “En el año XXXX tendrá
XX años”.
▪ Si edad_param se pasa y es menor que
self.edad, imprimir “No es posible realizar la
operación” y no calcular.
• Pruebas mínimas
o Instanciar al menos dos Empleado.
o Aplicar aumento_sueldo 2 veces y mostrar el sueldo
incrementado.
o Realizar una transferencia entre ambos empleados y mostrar
saldos antes y después de ambos
o Probar un caso de saldo insuficiente.
o Usar prediccion(...) con y sin edad_param inválido."""


class Persona:
    def __init__(self, nombre, edad, nacionalidad="peruana", saldo=0.0):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.saldo = saldo

    def actualizar_nombre(self, nombre):
        self.nombre = nombre
        print(f"Nombre actualizado a: {self.nombre}")

    def actualizar_edad(self, edad):
        if edad > 0:
            self.edad = edad
            print(f"Edad actualizada a: {self.edad}")
        else:
            print("Error: la edad debe ser mayor que 0.")

    def cumplir_anios(self):
        self.edad = self.edad+1
        print(f"¡Feliz cumpleaños! Ahora tienes {self.edad} años.")

    def mostrar_saldo(self):
        print(f"Saldo actual: S/ {self.saldo:  }")

    def transferir(self, destino, monto):
        if monto <= 0:
            print("El monto debe ser mayor que cero.")
        elif self.saldo < monto:
            print("Saldo insuficiente.")
        else:
            self.saldo -= monto
            destino.saldo += monto
            print(f"Transferencio exitosa de S/ {monto: } a {destino.nombre}.")
            print(f"Nueva saldo de {self.nombre}: S/ {self.saldo: }")
            print(f"Nuevo saldo de {destino.nombre}: S/ {destino.saldo: }")

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo, nacionalidad="peruana", saldo=0.0):
        super().__init__(nombre, edad, nacionalidad, saldo)
        self.sueldo = sueldo

    def aumento_sueldo(self):
        incremento = self.sueldo * 130/100
        self.sueldo += incremento
        print(f"Sueldo incrementado es Nuevo sueldo: S/ {self.sueldo:    }")


p1 = Persona("Johan", 25, saldo=200)
p2 = Persona("Ana", 22, saldo=100)

p1.transferir(p2, 50)

e1 = Empleado("Carlos", 30, 2500.0)
