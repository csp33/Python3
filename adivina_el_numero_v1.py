# v1: Juego en el que el usuario tendrá que adivinar un número aleatorio entre
# 0 y 100. Se añaden funciones.

# Función que pide un intento.
def pedir_numero():
    resultado=input("Introduzca un número entre 1 y 100.\n")
    try:
        resultado=int(resultado)
    except:
        resultado=pedir_numero()
    else:
        if resultado < 1 or resultado > 100:
            resultado=pedir_numero()
    return resultado

# Comenzamos importando la librería random
import random
# Generamos el número
numero=random.randint(0,100)
# Variable que nos dirá si hemos acertado
acertado=False
while not acertado:
    intento=pedir_numero()
    if intento < numero:
        print("¡Demasiado pequeño!")
    elif intento > numero:
        print("¡Demasiado grande!")
    else:
        acertado=True

print("¡Has superado el juego! El número era ",numero)
