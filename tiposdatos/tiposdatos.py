'''En Phyton, no hace falta declarar el tipo de las variables,
sino que cada valor tiene un tipo asignado
'''

#Numeros
entero = 1
decimal = 1.3
fracciones = 3/5  # Se puede expresar una operacion matematica


#Booleanos
esPar = True
esMayorEdad = False
negativo = (entero<0) #Se puede usar una expresion logica
entreCeroYCien = (entero>=0) and (entero<=100)
positivo = not(negativo)

#Cadenas
nombre = 'Angel Aguado'

#Tenemos el operador type para saber de que tipo es una variable
print(type(decimal))
print(type(esPar))
print(type(nombre))

#y el operador isinstance para saber si una variable es de un determinado tipo
print(isinstance(esPar, bool))