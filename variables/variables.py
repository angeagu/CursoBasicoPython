#Las variables permiten almacenar un valor, en un nombre que nos sirve como referencia

#Creamos una variable nombre de tipo texto
nombre = "Angel" #Utilizamos comillas dobles
apellido = 'Aguado' #Utilizamos comillas simples
direccion = """Plaza La Sal 3,
34005 Palencia
España"""

#y ahora una variable edad de tipo entero
edad = 39
"""Tambien podemos asignar variables indicando el tipo ,especialmente util para los numeros, en
caso de ser enteros o decimales"""
edad = int(39)
peso = float(83.5)
altura = float(1.87)

#Podemos utilizar las variables creadas en nuestros programas, por ejemplo, para mostrarlas por pantalla

print("Nombre: " + nombre + ", edad: " + str(edad)) #str indica a Python convertir la variable edad como texto

print("Peso: " + str(peso) +  "Altura: " + str(altura))
