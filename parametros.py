# -*- coding: utf-8 -*-

#  Funciones sin parametros

def saludar():
    print "Hola"

saludar()


# Funciones con parámetros posicionales

def saludar_a(nombre):
    print "Hola " + nombre  # concatenación

saludar_a("Ian")

# funciones con valor de retorno
def componer_nombre(nombre, apellido):
    return nombre.capitalize() + " " + apellido.capitalize()

nombre_completo = componer_nombre("CYNTHIA", "reMoLiNa")
print(nombre_completo)


# Detección de palindromo
def es_palindromo(palabra):
    # True si la palabra es un palíndromo
    # False si la palabra NO es un palíndromo
    palabra = palabra.lower()
    # quitar espacios
    reemplazos = {
        " ": "",
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
    }
    for viejo, nuevo in reemplazos.iteritems():
        palabra = palabra.replace(viejo, nuevo)

    # print("Comprobando: " + palabra[::-1])
    return palabra == palabra[::-1]

palindromo = "Anita lava la tina"
# print(palidromo)
print(es_palindromo(palindromo))
