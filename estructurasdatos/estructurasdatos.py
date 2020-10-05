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

# Insertamos un elemento en la lista en una posicion
impares.insert(2, 3);
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

# DICCIONARIOS - No hay orden, son estructuras de datos que asocian una clave a un valor.
dnis = {
    "71938134L": "Angel Aguado",
    "12443124M": "Diana Lopez",
    "72129837G": "Jesus de Juana",
}

# Operaciones habituales:
# Obtener un valor a partir de una clave:
print(dnis.get("71938134L"))

# Obtener un valor a portir de una clave y borrar esa clave y su valor asociado
dnis.pop("71938134L")
print(dnis)

# Añadir una nueva clave y valor, o modificar uno ya existente
dnis.update({"12456877M": "Antonio Martin"})
print(dnis)
dnis.update({"72129837G": "Maria Rodriguez"})
print(dnis)

# Comprobar si hay una key en un diccionario
print("72129837G" in dnis)
# Comprobar si hay un valor en un diccinonario
print("Antonio Martin" in dnis.values())

# CONJUNTOS
conjunto = {"Pedro Perez", "Lucia De Miguel", "Maria Fernandez"}
print(conjunto)

# Operaciones
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {3, 5, 7}
# Interseccion
print(conjunto1 & conjunto2)
# Union
print(conjunto1 | conjunto2)
# Diferencia
print(conjunto1 - conjunto2)
