# Escribir una funcion que a partir del alto y ancho de un rectangulo, muestre por pantalla
# Su area y su perimetro.
# def rectangulo(alto, ancho):
#     print("Area: " + str(alto * ancho))
#     print("Perimetro: " + str(alto*2 + ancho*2))
#
# rectangulo(12,4)

# Crear una funcion que almacene en un array 10 números enteros.
# Imprime por pantalla los elementos que ocupan las posiciones pares y su suma
# Lo mismo para las posiciones impares.
# def sumaParesImpares():
#     sumaPares = 0
#     sumaImpares = 0
#     lista = [1,2,3,4,5,6,7,8,9,10]
#     for indice, numero in enumerate(lista):
#         if((indice+1)%2 ==0):
#             sumaPares += numero
#         else:
#             sumaImpares += numero
#     print("Suma Pares: " + str(sumaPares))
#     print("Suma Impares: " + str(sumaImpares))
#
# sumaParesImpares()

# Escribir una funcion que Verifique si una cadena de texto almacenada, es un DNI correcto o no.
# Si lo es, se devolvera true y si no lo es, se devolvera false.
# Los DNI tienen 8 dígitos y, a continuación una letra (no importa que sea mayúscula o minúscula).
# def validaDNI(dni):
#     valido = True
#     cad = str(dni)
#     if not cad[0:len(cad)-1].isdigit():
#         valido = False
#     else:
#         if not cad[len(cad)-1].isalpha():
#             valido = False
#     return valido
#
# print(validaDNI("124A1242Z"))
# print(validaDNI("71938103Z"))


# Crear una funcion que tome como entrada dos cadenas y devuelva el numero de caracteres que tienen
# # en comun las dos cadenas.
# def caracteresComunes(cad1,cad2):
#     comunes = 0
#     for letra in cad1:
#         if cad2.find(letra)!=-1:
#             comunes += 1
#     return comunes
#
# print(caracteresComunes("Valladolid","Dario"))


# Modificar la funcion anterior para que en lugar del numero de caracteres en comun, devuelva los
# caracteres que tienen en comun.
# def caracteresComunes(cad1,cad2):
#     comunes = '';
#     for letra in cad1:
#         if cad2.find(letra)!=-1 and comunes.find(letra)==-1:
#             comunes += letra
#     return comunes
#
# print(caracteresComunes("Valladolid","Dario"))


# Crear una funcion que indique si una palabra es abedeceira. Una palabra es abecedeira si todas
# sus letras estan ordenadas en orden alfabetico.
# def abecedeira(palabra):
#     palabra = palabra.lower()
#     abecedeira = True
#     indice = 0
#     while(indice < len(palabra)):
#         if indice < len(palabra)-1 and ord(palabra[indice]) > ord(palabra[indice+1]):
#             abecedeira = False
#         indice += 1
#     return abecedeira
#
# print(abecedeira("Aguado"))
# print(abecedeira("Bello"))