# -*- coding: utf-8 -*-

#  lista_valores = [10, 100, 90.9, 100]
# suma_total / numero_elementos
def promedio(lista_valores):
    promedio = sum(lista_valores) / len(lista_valores)
    return promedio

# moda -> valor que más se repite

def moda(lista_valoras):
    valores = {}
    for valor in lista_valores:
        if valores.get(valor):
            valores[valor] += 1
        else:
            valores[valor] = 1

    # print(valores)

    v_max = 0
    moda = 0
    for valor, repeticiones in valores.iteritems():
        if repeticiones > v_max:
            v_max = repeticiones
            moda = valor

    return moda

# valor que está exactamente a la mitad de la muestra ordenada
# si es par el promedio de los dos centrales

def mediana(lista_valores):
    # ordenar la lista
    # detectar si es par o impar
    # par: devolver promedio de centrales
    # impar: valor central

    lista_valores.sort()
    if len(lista_valores) % 2:

    return mediana


lista_valores = [10, 100, 90.9, 100, 3, 3, 3]
print(moda(lista_valores))
