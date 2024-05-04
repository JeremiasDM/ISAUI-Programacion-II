import random
import string

def generar_contrasena(longitud = 12):
    caracters = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracters) for _ in range(longitud))
    return contrasena

longitud_deseada = int(input("Porfavor indique cuantos caracteres debe tener la Contraseña:"))
nueva_contraseña = generar_contrasena(longitud_deseada)
print(f"Esta es su nueva contraseña: {nueva_contraseña}")


def run():

    generar_contrasena()
    