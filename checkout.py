# -*- coding: utf-8 -*-
#checkout
# __init__.py
from productos import ProductoFisico

class Checkout:

    def obtener_total(self, lista_productos):
        total = 0
        for producto in lista_productos:
            total += producto.precio
        return total

    def imprimir_lista(self, lista_productos):
        # imprimir productos con sku, precio y total
        pass


checkout = Checkout()
tele = ProductoFisico("tele", "100", 100)
radio = ProductoFisico("Radio", "105", 50)
comp = ProductoFisico("Computadora", "110", 1000)

lista_productos = [tele, radio, comp]

print(checkout.obtener_total(lista_productos))
