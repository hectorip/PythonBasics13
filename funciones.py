# -*- coding: utf-8 -*-
# Funciones

# grupo = [
#    'toño': {'nombre': 'Antonio', 'edad': 41},
#    'jimmy': {'nombre': 'Ximena', 'edad': 24}
# ]
def imprimir_grupo(grupo):
    # grupo
    for alumno in grupo:
        for dato, valor in alumno.iteritems():
            print(dato + " es " + str(valor))

batch_13 = [
    {'nombre': 'Antonio', 'edad': 41},
    {'nombre': 'Ximena', 'edad': 24}
]

imprimir_grupo(batch_13)
