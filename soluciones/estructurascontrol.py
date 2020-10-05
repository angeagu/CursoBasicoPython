# Escribir una sentencia if-else que visualice la palabra “Alta” si el valor de una
# variable nota es mayor que 100 y ”Baja“ si el valor de esa nota es menor que 100.
# nota = 5
# if (nota > 100):
#     print("Alta")
# else:
#     print("Baja")


# Escribir un programa Binario que lea tres números. Estos números deberán ser o 0 o 1,
# de modo que si el usuario introduce otro número distinto a 0 o 1 el programa finalizará
# mostrando al usuario un mensaje de cómo debe ejecutarse dicho programa.
# El programa debe tratar estos números como si se tratasen de un número binario de tres bits
# y mostrar su valor en decimal.
# indice = int(1);
# numero1 = int(0);
# numero2 = int(0);
# numero3 = int(0);
# while (indice <= 3):
#     num = int(input("Introduzca digito binario "));
#     if (num > 1):
#         exit("Se deben introducir tres digitos binarios (0,1)")
#     else:
#         if (indice == 1):
#             numero1 = num;
#         elif (indice == 2):
#             numero2 = num;
#         elif (indice == 3):
#             numero3 = num;
#     indice += 1;
# print("Numero en decimal: " + str((numero3 * 4) + (numero2 * 2) + numero1));

#Cuatro números enteros entre 0 y 100 representan las puntuaciones de un estudiante de informática
# a lo largo del curso.Escribir un programa llamado MiNota para encontrar la media de estas puntuaciones
# numero1 = 12
# numero2 = 46
# numero3 = 44
# numero4 = 87
# suma = numero1 + numero2 + numero3 + numero4
# media = suma/4;
# print("Media: " + str(media));

# Escribir un programa Asteriscos1 que muestre el siguiente dibujo, pudiendo
# pintar solamente un ‘*’ cada vez y haciendo uso de bucles.

# Escribir una programa Asteriscos2 que muestre la siguiente figura, pudiendo
# pintar solamente un ‘*’ cada vez y haciendo uso de bucles.

# Escribir un programa Potencias que mediante un bucle while visualice todas las
# potencias de un número escogido entre 1 y 10 y que sean menores que 1000.
# num = int(input("Introduzca numero entre 1 y 10"))
# if (num > 10 or num < 0):
#     exit("El numero no esta entre 1 y 10")
# else:
#     exponente = 0
#     potencia = 0
#     while (potencia < 1000):
#         potencia = pow(num, exponente)
#         if (potencia < 1000):
#             print(str(num) + "elevado a " + str(exponente) + " = " + str(potencia))
#         exponente += 1

# Crear un programa que lea un numero y calcule su factorial.
# numero = int(input("Introduzca numero: "))
# resultado = 1
# while(numero!=1):
#     resultado *= numero
#     numero = numero - 1
# print("El factorial es: " + str(resultado))