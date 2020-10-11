#Cadenas en python

#Parsear un dato como cadena
numero = 3
cadena = str(numero)

#Obtener la longitud de una cadena
cadena = 'Maravilla'
len(cadena)

#Acceder a una letra de cadena
print(cadena[2])

#Recorrer una cadena
for letra in cadena:
    print(letra)

print(cadena.capitalize())
print(cadena.casefold())
print(cadena.upper())
print(cadena.count("a"))
print(cadena.endswith("villa"))
print(cadena.startswith("mir"))
print(cadena.find("vi"))
print(cadena.format())
print(cadena.index("ra"))
print(cadena.isalnum())
print(cadena.isdecimal())
print(cadena.isdigit())
print(cadena.islower())
print(cadena.isupper())
print(cadena.isnumeric())
print(cadena.join(["otra"," ", "maravilla"]))
print(cadena.strip())
print(cadena.replace("Mara","Bere"))
print(cadena.rsplit(" "))
print(cadena.swapcase())
