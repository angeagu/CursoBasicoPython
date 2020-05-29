#ESTRUCTURAS DE CONTROL ITERATIVAS

#BUCLE WHILE
vuelta=1
while vuelta<10:
    print("Vuelta: " + str(vuelta))
    vuelta = vuelta + 1


#BUCLE FOR - IN
for vuelta in range(1,5):
    print(str(vuelta))

numeros = [1,3,5,7,9]
for numero in numeros:
    print(numero)

for i, num in enumerate(numeros):
    print("Posicion " + str(i) + ": " + str(num))
