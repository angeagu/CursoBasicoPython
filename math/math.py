# el modulo math nos da acceso a la libreria de funciones matemáticas
import math
import random
import statistics

print("Factorial de 5: " + str(math.factorial(5)))
print(math.floor(4.5))
print(math.ceil(4.5))
print(math.pow(3,2))
print(math.sqrt(144))
radio = 4
perimetroCirculo = 2 * math.pi * radio

print("Numero aleatorio: " + str(random.random()))
print("Numero aleatorio del uno al diez: " + str(random.randrange(10)))
print("3 Numeros aleatorios del 1 al 20: " + str(random.sample(range(20),3)))

print("Media: " + str(statistics.mean([1,4,5,6])))
print("Mediana: " + str(statistics.median([1,4,5,6])))

