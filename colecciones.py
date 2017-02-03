# -*- coding: utf-8 -*-

batch_13 = ["Alejandro@devf.mx", "Frank", "Sebastián", "Nelly", "Cynthia"]

elementos = 'aire', 'viento', 'tierra', 'fuego'

# iterables

for alumno in batch_13:
    print(alumno)

# Range [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Range -> inicio, fin(exclusivo), step(opcional)
for i in range(0, 10):
    print(i)

for elemento in elementos:
    print(elemento)

persona = {
    "nombre": "Héctor",
    "apellido": "Patricio",
    "edad": (27, "estas muy viejo")
    # "27": "estas muy viejo"
}
print("Diccionario =========")

for dato, valor in persona.iteritems():
    print(dato + " es " + str(valor))

# for elemento_individual in iterable:
#   le hago algo
