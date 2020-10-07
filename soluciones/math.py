import math
import random
import statistics
# Crea un programa que genere 5 aleatorios entre 5 y 25
print(str(random.sample(range(5,25),5)))

# Mostrar por pantalla:
# Un número al azar entre 0 y 1: 0.9933584384998737
print(str(random.random()))
# Un número al azar entre 50 y 150: 52
print(str(random.randrange(50,150)))

# Seno de 45 grados: 0.7071067811865475
print(math.sinh(45))
# Raíz cuadrada de 36: 6.0
print(math.sqrt(36))
# Cinco elevado al cubo: 125.0
print(math.pow(5,3))
# Mayor valor entre 2 y 3: 3
print(max([2,3]))
# Valor absoluto de -4,5: 4.5
print(math.fabs(-4.5))
# Menor entero más cercano a -4,5: -5.0
print(math.ceil(-4.5))
# Mayor entero más cercano a -4,5: -4.0
print(math.floor(-4.5))
# Crear un programa que lea un numero y nos diga si el numero es primo o no.
# numero = int(input("Introduzca un numero: "))
# primo = True
# for index in range(2,numero):
#     if (numero % index == 0):
#         primo = False
# print("Es primo" if primo else "No es primo")

# Crear un programa que pase un número a binario.
numero = int(input("Introduzca un numero: "))
binario = ''
while(numero>=1):
    binario = str(numero%2) + binario
    numero = int(numero/2)

print('Binario: ' + binario)