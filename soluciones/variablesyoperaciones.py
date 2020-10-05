# Escribir un programa TablaMultiplicar que escriba por pantalla la tabla de multiplicar
# de un número introducido por teclado.
# numero = int(input("Introduzca numero: "));
# for indice in range(1, 11):
#     print(str(numero) + "x" + str(indice) + "= " + str(numero * indice));


# Escribir un programa Minutos que convierta un número dado de segundos en su
# equivalente en minutos y segundos. Ejemplo: 128 s = 2 m 8 s.
# numero = int(input("Introduzca numero: "));
# minutos = int(numero/60);
# segundos = int(numero%60);
# print("Minutos: " + str(minutos) + " segundos: " + str(segundos));


# Escribir un programa EstanEnOrden que reciba tres enteros desde el teclado y
# digan si están ordenados o no.
# numero1 = int(input("Introduzca numero1: "));
# numero2 = int(input("Introduzca numero2: "));
# numero3 = int(input("Introduzca numero3: "));
# if(numero1 <= numero2 and numero2 <= numero3):
#     print("Los numeros estan ordenados de menor a mayor")
# elif(numero1 >= numero2 and numero2 >= numero3):
#     print("Los numeros estan ordenados de mayor a menor")
# else:
#     print("Los numeros no estan ordenados")

# Escribir un programa SentenciaLogica que a través de una
# sentencia lógica (boolean) clasifique un entero x en una de las siguientes categorías:
# x < 0 o bien 0 x 100 o bien x > 100
# numero = int(input("Introduzca numero: "));
# if (numero < 0):
#     print("Numero negativo")
# elif (numero >= 0 and numero <= 100):
#     print("Numero entre 0 y 100")
# else:
#     print("Numero mayor que 100");

# Escribir un programa DiasDelMes, que reciba desde el teclado el número de un mes (del 1 al 12)
# y muestre el número de días de ese mes (febrero 28 días).


# Escribir un programa Bisiesto que determine si un año es bisiesto. Un año es bisiesto si es múltiplo de 4
# (por ejemplo 1984). Sin embargo los años múltiplos de 100 sólo son bisiestos cuando a la vez son múltiples de 400 (por ejemplo 1800 no es bisiesto, mientras que 2000 si lo es).
# año = int(input("Introduzca año: "));
# if (año % 4 == 0):
#     if (año % 100 == 0):
#         if (año % 400 == 0):
#             print("Bisiesto")
#         else:
#             print("No Bisiesto")
#     else:
#         print("Bisiesto")
# else:
#     print("NO Bisiesto")
#
