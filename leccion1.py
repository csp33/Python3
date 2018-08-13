
# Comenzamos con el clásico "Hola mundo".
print("Hello world!")

# Ahora pasamos a la entrada de datos por teclado.

print("***Probando entrada por teclado***")
entrada = input("Introduzca un dato:\n")
print("Ha introducido",entrada)

# Algunas operaciones con booleanos.

print("***Probando booleanos***")
primer = input("Introduzca un número:\n")
segundo = input("Introduzca otro número:\n")
mayor = primer > segundo
menor = primer < segundo
igual = primer == segundo
distinto = primer != segundo
print(primer,">",segundo,":",mayor)
print(primer,"<",segundo,":",menor)
print(primer,"=",segundo,":",igual)
print(primer,"!=",segundo,":",distinto)

# En el ejemplo anterior, 42>8 : True (se comparaban como cadenas de caracteres)
# Para evitarlo, transformamos a int la entrada.

print("***Probando entrada por teclado con conversión a int***")
primer = int(input("Introduzca un número:\n"))
segundo = int(input("Introduzca otro número:\n"))
mayor = primer > segundo
menor = primer < segundo
igual = primer == segundo
distinto = primer != segundo
print(primer,">",segundo,":",mayor)
print(primer,"<",segundo,":",menor)
print(primer,"=",segundo,":",igual)
print(primer,"!=",segundo,":",distinto)

# Introducimos las excepciones.

print("***Probando excepciones***")
import sys
numero = input("Introduce un número:")
try:
    numero = int(numero)
except:
    print("Conversión errónea. Saliendo...",file=sys.stderr)
    sys.exit()

# Vamos con los condicionales:

print("***Probando condicionales***")

primero = int(input("Introduzca el primer número:"))
segundo = int(input("Introduzca el segundo número:"))
if primero > segundo:
    print(primero,">",segundo)
elif segundo < primero:
    print(primero,"<",segundo)
else:
    print(primero,"=",segundo)

if 1 <= primero <= 10:
    print(primero,"está entre 1 y 10")
else:
    print(primero,"no está entre 1 y 10")

if 1 <= segundo <= 10:
    print(segundo,"está entre 1 y 10")
else:
    print(segundo,"no está entre 1 y 10")

# Ahora, los bucles. La idea es solicitar un número entre 1 y 10 y no salir del
# bucle hasta que no se cumpla la condición.

print("***Probando bucles***")

numero = input("Introduzca un número entre 1 y 10:\n")
try:
    numero = int(numero)
except:
    numero = 0 # Si no se introduce un número, tomamos el 0

while not 1 <= numero <= 10:
    numero = input("Introduzca un número entre 1 y 10:\n")
    try:
        numero = int(numero)
    except:
        numero = 0 # Si no se introduce un número, tomamos el 0
print("En este punto del programa estamos seguros de que ",numero,"es un número\n",
" y está comprendido ente 1 y 10.")

# Hacemos lo anterior pero evitando duplicar el código de entrada:

print("***Probando bucles infinitos***")

while True:
    # Pedimos el número
    numero = input("Introduzca un número entre 1 y 10:\n")
    try:
        numero = int(numero)
    except:
        pass # No hacemos nada, ya que se volverá a ejecutar el bucle.
    else:   #Else acompañando a try. Se ejecuta cuando no hay excepción.
        #Comprobamos
        if 1 <= numero <= 10:
            #No necesitamos iterar más, así que salimos.
            break
print("En este punto del programa estamos seguros de que ",numero,"es un número\n",
" y está comprendido ente 1 y 10.")
