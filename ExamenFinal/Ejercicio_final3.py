
import datetime

def conteo(func):

    def wrapper(*args, **kwargs):
        num_params = len(args) + len(kwargs)
        print(f"\n--- Decorador 'conteo' para '{func.__name__}' ---")
        print(f"Número de parámetros usados: {num_params}")

        if num_params > 1:
            print(f"Procesando lógica de '{func.__name__}'...")
            result = func(*args, **kwargs)
            print(f"Decorador 'conteo': La función '{func.__name__}' fue ejecutada exitosamente.")
            return result
        else:
            print(f"Decorador 'conteo': Se requiere más de 1 parámetro para procesar la lógica de '{func.__name__}'.")
            return None
    return wrapper

def register_student(nombre: str, edad: int, nota1: float, nota2: float, nota3: float, nota4: float):

    now = datetime.datetime.now()
    hora = now.hour
    minuto = now.minute

    print(f"{nombre} de {edad} años ha sido registrado a las {hora} horas con {minuto} minutos.")

    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"La media de las notas de {nombre} es: {media:.2f}")
    return media

def greet_user(name: str = "Invitado"):

    print(f"Hola, {name}! Bienvenido.")
    return f"Saludo a {name}"
