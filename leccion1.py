
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
numero=input("Introduce un número:")
try:
    numero=int(numero)
except:
    print("Conversión errónea. Saliendo...",file=sys.stderr)
    sys.exit()

# Vamos con los condicionales:

print("***Probando condicionales***")

primero=int(input("Introduzca el primer número:"))
segundo=int(input("Introduzca el segundo número:"))
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

# Ahora, los bucles
