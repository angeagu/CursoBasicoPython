# ESTRUCTURAS DE CONTROL , sirven para modificar el flujo de ejecucion de un programa.

# CONDICIONALES
numero = 5
if (numero == 5):
    print("es un cinco")
else:
    print("es otro numero")

# EJEMPLO Comprobar si un numero es par o impar
numero = 7
if (numero % 2 == 0):
    print("es un numero par")
else:
    print("es un numero impar")

# OPERADORES BOOLEANOS <, >, not, and, or
if (numero > 0):
    print("El numero es mayor que 0")

if (numero < 0):
    print("El numero es negativo")

if (numero > 1 and numero < 10):
    print("El numero esta entre 0 y 10")

# Asignacion de una variable
par = True if (numero % 2 == 0) else False
