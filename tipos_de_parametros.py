# -*- coding: utf-8 -*-

def precio_final(precio=0, tasa_iva=0.16):
    return precio * (1 + tasa_iva)

p = 10000
print(precio_final(tasa_iva=0.18, precio=1000))

def imprimir_lista_de_productos(*args):
    # args es un lista [],  de todos los par´åmetros que recibe
    for producto in args:
        print(producto)

imprimir_lista_de_productos("silla", "mesa", " sillón")

def aplicar_impuestos(precio, **kwargs):
    total_impuestos = 0
    for impuesto, tasa in kwargs.iteritems():
        impuesto_actual = precio * tasa
        total_impuestos = total_impuestos + impuesto_actual
        print(impuesto + " es " + str(impuesto_actual))
        print(total_impuestos)
    return precio + total_impuestos

aplicar_impuestos(1000,iva=0.16, ipsss=0.04, isr=0.18, ietu=.05, iii=.10)
