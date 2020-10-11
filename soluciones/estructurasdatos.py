# Visualizar los datos de cada una de las colecciones.
# Añade a la primera colección todos los hijos que tiene la segunda y
# visualiza los datos de la primera colección.
# Borra de la primera colección todos los hijos que no estén en la segunda colección y
# visualiza los datos de la primera colección.
# lista1 = [4,5,6,7,8,9]
# lista2 = [1,2,5,6,10,11]
#
# print(lista1)
# print(lista2)
# lista1.extend(lista2)
# print(lista1)
# for indice,numero in enumerate(lista1):
#     if numero not in lista2:
#         del lista1[indice]
# print(lista1)

#
# Crea un programa Frases que almacene en un array unidimensional 5 frases que se introducen por teclado. Diseña los siguientes métodos:
# a. imprimeFrases: imprime por pantalla el contenido del array.
# b. mayorFrase: imprime por pantalla la frase de mayor longitud y la posición que ocupa en el array.
# c. menorFrase: imprime por pantalla la frase más pequeña y la posición que ocupa.

# Crear una funcion que tome como entrada dos listas del mismo tamaño y genere como
# resultado una lista que es la suma de las listas.
# def sumaMatrices(matriz1,matriz2):
#     resultado = [[0 for x in range(len(matriz1))] for x in range(len(matriz1[0]))]
#     for fila in range(len(matriz1)):
#         for columna in range(len(matriz1[0])):
#             resultado[fila][columna] = matriz1[fila][columna] + matriz2[fila][columna]
#     return resultado
#
# m1 = [[1,2,4],[5,3,1],[6,3,9]]
# m2 = [[2,4,5],[5,6,6],[9,8,7]]
# print(sumaMatrices(m1, m2))


# Crear una funcion que tome como entrada una matriz y calcule la matriz resultante de
# calcular para cada posicion la media de su fila y columna.
# matriz = [[2,4,5],[5,6,6],[9,8,7]]
# for fila in range(len(matriz)):
#     for columna in range(len(matriz[0])):
#         print(matriz[fila][columna])

#
# Escribe un programa Matriz1 que genere un array bidimensional 5x5, de tal forma que sus filas pares sean múltiplos de 2 y las impares sean múltiplos de 3. Además diseña los siguientes métodos:
# a. imprimirMatriz: muestra por pantalla la matriz creada.
# b. sumaMatriz: muestra la suma de todos sus elementos.
# c. diagonal: imprime los elementos de su diagonal principal.