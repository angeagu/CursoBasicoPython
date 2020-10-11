#Crea un programa que partiendo de la cadena "Somos de Fonetic, somos los mejores"
# declarada e inicializada como variable primitiva, mostrar por consola lo siguiente:
# Su longitud
# El carácter asociado al índice 7
# La subcadena "Fonetic"
# Las veces que se repite la letra 's'
# La cadena transformada en mayúsculas
# Comprobar si el primer carácter de la cadena es 'M' y mostrar por consola un mensaje que lo indique.
#
# cadena = 'Somos de Fonetic, somos los mejores'
# print('Longitud de la cadena: ' + str(len(cadena)))
# print(cadena[6])
# print(cadena[9:16])
# print("Numero de s: " + str(cadena.count("s")))
# print(cadena.upper())
# print("Empieza por M: " + str(cadena.startswith("M")))

# Realiza un programa que invierta los caracteres de una cadena dada, de tal forma,
# que los caracteres en mayúsculas los convierta en minúsculas y viceversa.
# cadena = "Esta Es una PruebA BasiCa"
# print("Version 1: " + str(cadena.swapcase()))
#
# cadenaConvertida = '';
# for letra in cadena:
#     if(letra.isupper()):
#         cadenaConvertida += letra.lower()
#     else:
#         cadenaConvertida += letra.upper()
# print('Cadena Convertida: ' + cadenaConvertida)


# Realiza un programa que dada una frase cuente cuántas vocales hay.
# cadena = 'murcielago'
# numVocales = 0;
# print(str("aeiou".find("r")))
# for letra in cadena:
#     if "aeiou".find(letra) != -1:
#         numVocales += 1
# print("NumVocales: " + str(numVocales))

#  Programa que pide introducir una cadena de caracteres por teclado y que letra a buscar
#  y visualiza por pantalla el número veces que contiene dicha letra en la cadena.

# cadena = input("Introduzca cadena: ")
# letra = input("Introduzca letra a buscar: ")
# print("Hay " + str(cadena.count(letra))  + " ocurrencias de la letra " + letra)

# Crea un programa que compruebe si un número es capicúa.
# num = input("Introduzca numero: ")
# num_list=list(num)
# if num_list == num_list[::-1]:
#     print(''.join(num_list) + " es capicua")
# else:
#     print(''.join(num_list) + " NO es capicua")


# Crear un programa para transformar una cadena a codigo ASCII.
# cadena = "Prueba"
# ascii = []
# for letra in cadena:
#     ascii.append(ord(letra))
# print(ascii)

# Escribe un programa que imprima las letras de una frase introducida por teclado de una forma
# alternativa, es decir, una de la parte final y la siguiente de la inicial,
# hasta recorrer todos los caracteres de la misma.

# Realiza un programa que cuente las veces que aparece una frase en otra,
# ambas introducidas por teclado, y que muestre las posiciones en las que se encuentra.

#Escribe un programa que invierta los dígitos de un entero dado.


# Verificar si una cadena de texto almacenada, es un DNI correcto o no.
# Si lo es, se mostrará por consola su parte numérica;
# si no lo es se mostrará el mensaje "DNI incorrecto".
# Se tendrá en cuenta que el DNI tienen 8 dígitos y, a continuación, una letra (no importa que sea mayúscula o minúscula).