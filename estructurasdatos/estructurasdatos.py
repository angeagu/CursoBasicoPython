"""Tipos de Estructuras de Datos, estructuras que nos permiten guardar en una
variable, varios valores, como por ejemplo una lista"""

# Vamos a ver dos tipos, listas y diccionarios

# LISTAS - Elementos que tienen un orden, se tiene en cuenta la posicion en la que esta el elemento
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
impares = [1, 3, 5, 7]
elementos = [1, "dos", 3, "cuatro"]  # Las listas pueden contener cualquier tipo de variables

print("Dias de la semana")
print(dias)

# Operaciones habituales

# Acceso a un elemento
print("Fin de semana: " + dias[5] + ", " + dias[6])

# Añadimos un elemento al final de lista de impares
impares.append(9)
print(impares)

# Borramos un elemento de la lista
impares.remove(3)
print(impares)

# Borramos un elemento de la lista por posicion
del impares[0]
del elementos[2:4] #Borra del elemento x al y-1
print(elementos)

# Insertamos un elemento en la lista en una posicion
impares.insert(2, 3);
impares.insert(1, 1);
print(impares)

# Obtenemos un elemento de la lista, sacandolo de la misma
nueve = impares.pop(4)
print(impares)

# Añadimos varios elementos al array
impares.extend([11, 13, 15])  # Extend no admite un unico valor como append, sino un array
print(impares)

# Concatenar dos listas
pares = [2, 4, 6, 8]
impares.extend(pares)
print(impares)

# Obtener una sublista
dosPrimerosPares = pares[0:2]
ultimosPares = pares[2:4]

# ordenar una lista
diasOrdenadosAlfabeticamente = sorted(dias)
print(diasOrdenadosAlfabeticamente)

# Comprehensions - Brackets que contienen una expresion for, seguida de una o más cláusulas for o if
ceroADiez = [num for num in range(10)]
print('Cero a Diez: ' + str(ceroADiez))
cuadrados = [num**2 for num in range(15)]
print('Lista Cuadrados: ' + str(cuadrados))
cuadradosMenores100 = [num for num in cuadrados if num < 100]
diasMayusculas = [dia.upper() for dia in dias]

#Recorrer una lista
for num in impares:
    print(num)

for indice, valor in enumerate(cuadrados):
    print("Cuadrado de: " + str(indice) + " valor: " + str(valor))

# Recorrer sobre dos secuencias al mismo tiempo, emparejando sus entradas
nombres = ['Angel','Alvaro','Ignacio']
apellidos = ['Aguado Andres', 'Cuadrado Ortega', 'Diez Perez']
for nombre,apellido in zip(nombres,apellidos):
    print("Nombre Completo: " + nombre + " " + apellido)

#Recorrer una lista en orden inverso
for num in reversed(pares):
    print(num)


# DICCIONARIOS - No hay orden, son estructuras de datos que asocian una clave a un valor.
dnis = {
    "71938134L": "Angel Aguado",
    "12443124M": "Diana Lopez",
    "72129837G": "Jesus de Juana",
}

# Operaciones habituales:
# Obtener un valor a partir de una clave:
print(dnis.get("71938134L"))
print(dnis['72129837G'])
# Obtener un valor a portir de una clave y borrar esa clave y su valor asociado
dnis.pop("71938134L")
print(dnis)

# Añadir una nueva clave y valor, o modificar uno ya existente
dnis.update({"12456877M": "Antonio Martin"})
dnis["71828333M"] = "Pedro Salazar"
print(dnis)
dnis.update({"72129837G": "Maria Rodriguez"})
print(dnis)

# Borrar una clave y su valor asociado
del dnis['71828333M']
print(dnis)

#Obtener una lista con las claves del diccionario
claves = list(dnis) #Obtiene las claves del diccionario por orden de inserción
print(claves)
claves = sorted(dnis)
print(claves) #Obtiene las claves del diccionario por orden alfabetico

# Comprobar si hay una key en un diccionario
print("72129837G" in dnis)
# Comprobar si hay un valor en un diccinonario
print("Antonio Martin" in dnis.values())

#Comprehensions también se utilizan para construir diccionarios
cuadrados = {x: x**2 for x in (2, 4, 6)}

#Recorrer diccionarios
for clave, valor in dnis.items(): #Items devuelve cada uno de los registros del diccionario
     print(clave, valor
           )

# CONJUNTOS - Coleccion de elementos que: a) No hay duplicados, b) No hay orden (por lo tanto no hay
# acceso por posición)

conjunto = {"Pedro Perez", "Lucia De Miguel", "Maria Fernandez"}
print(conjunto)
otroconjunto = set('creamosUnConjuntoApartirDeUnaCadenaParaDescartarLetrasDuplicadas')
print (otroconjunto)

# Operaciones
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {3, 5, 7}

#Pertenencia
print(4 in conjunto1)
print(9 in conjunto2)

conjunto1.add(6)
conjunto1.add(7)
conjunto1.add(5)
print(conjunto1) #Los duplicados vemos que son borrados.
# Interseccion
print(conjunto1 & conjunto2)
# Union
print(conjunto1 | conjunto2)
# Diferencia
print(conjunto1 - conjunto2)
# XOR - En uno u otro pero no en los dos
print(conjunto1 ^ conjunto2)