'''FUNCIONES - Bloque de codigo que agrupa varias sentencias de codigo, que puede ser llamado desde
otro punto del programa. Puede necesitar una serie de parametros para funcionar y puede devolver un valor
'''


def esPar(numero):
    '''indica si un numero es par
        :argument numero
        :return boolean indicando si el numero es par
    '''
    return numero % 2 == 0


def sumaNumeros(arrayNumeros):
    '''Devuelve la suma de un array de numeros
        :argument array de numeros
        :return suma de los numeros del array
    '''
    suma = 0
    for numero in arrayNumeros:
        suma = suma + numero
    return suma


def esMayor(num1, num2):
    '''Devuelve el mayor de dos numeros
        :argument numero1
        :argument numero2
        :return mayor de los dos numeros
    '''
    return num1 if (num1 > num2) else num2


print('5 es par: ' + str(esPar(5)))
print('6 es par: ' + str(esPar(6)))
print('Suma de numeros: ' + str(sumaNumeros([1, 2, 3, 4, 5])))
print('EsMayor-> 7,9: ' + str(esMayor(7, 9)))
print('EsMayor-> 7,9: ' + str(esMayor(num2=7, num1=9)))
