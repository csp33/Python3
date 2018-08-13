# v0: Juego en el que el usuario tendrá que adivinar un número aleatorio entre 0 y 100.

# Comenzamos importando la librería random
import random
# Generamos el número
numero=random.randint(0,100)
# Variable que nos dirá si hemos acertado
acertado=False
while not acertado:
    intento=input("¡Adivine el número!\n")
    try:
        intento=int(intento)
    except:
        pass #Si no es un número se vuelve a pedir
    else:
        if intento < 1 or intento > 100:
            print("El número está entre 1 y 100.")  #Si nos salimos del rango
        else:
            if intento < numero:
                print("¡Demasiado pequeño!")
            elif intento > numero:
                print("¡Demasiado grande!")
            else:
                acertado=True

print("¡Has superado el juego! El número era ",numero)
