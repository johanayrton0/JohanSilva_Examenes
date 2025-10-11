import random
import datetime


def generar_numero_aleatorio():
    return random.randint(1, 50)


def pedir_y_validar_numero():

    while True:
        try:
            entrada = input("Ingresa un número entero (entre 1 y 99): ")

            numero_ingresado = int(entrada)

            if 0 < numero_ingresado < 100:
                return numero_ingresado
            else:
                print(" El número debe ser mayor que 0 y menor que 100.")

        except ValueError:
            print("La entrada no es un número entero válido.")


def decorar_victoria(func):

    def envoltura(numero_a_adivinar):
        print(" Validando Intento ")


        resultado = func(numero_a_adivinar)

        print("  Validacion Lista.")

        return resultado

    return envoltura


@decorar_victoria
def validar_adivina(numero_secreto):

    while True:
        numero_ingresado = pedir_y_validar_numero()

        if numero_ingresado == numero_secreto:
            return True  # El usuario ha adivinado
        elif numero_ingresado < numero_secreto:
            print("El número secreto es MAYOR que tu intento.")
        else:  # numero_ingresado > numero_secreto
            print("El número secreto es MENOR que tu intento.")


def adivina():

    print("Intenta adivinar el número entre 1 y 50.")


    numero_a_adivinar = generar_numero_aleatorio()



    validar_adivina(numero_a_adivinar)

    ahora = datetime.datetime.now()

    dia = ahora.day
    mes = ahora.month
    hora = ahora.hour
    minuto = ahora.minute

    print("\n HAS GANADO!")
    print(f"Acertaste el número secreto *{numero_a_adivinar}*.")
    print(f"El acierto ocurrió el *día {dia}, del **mes {mes}, a las *{hora}* horas y *{minuto}** minutos.")
