# -*- coding: utf-8 -*-
#checkout
# __init__.py
from productos import ProductoFisico
from metodos import Stripe, Bitcoin

class Checkout:

    def __init__(self, metodo_de_pago):
        self.metodo_de_pago = metodo_de_pago
        # self.mailer = mailer


    def obtener_total(self, lista_productos):
        total = 0
        for producto in lista_productos:
            total += producto.precio
        return total

    def imprimir_lista(self, lista_productos):
        # imprimir productos con sku, precio y tota
        for producto in lista_productos:
            print("Nombre: %s, SKU: %s, Precio: %s" % (producto.nombre, producto.sku, producto.precio))

    def cobrar(self, lista_productos):
        total = self.obtener_total(lista_productos)
        self.metodo_de_pago.cobrar(total)
        print("He cobrado %s" % total)

    # def cobrar(self, lista_productos):
    #     print("estoy cobrando con stripe")
    #
    # def cobrar2(self, lista_productos):
    #     print("estoy cobrando con MP")


tele = ProductoFisico("tele", "100", 100)
radio = ProductoFisico("Radio", "105", 50)
comp = ProductoFisico("Computadora", "110", 1000)
lista_productos = [tele, radio, comp]


checkout_stripe = Checkout(Stripe)
checkout_stripe.cobrar(lista_productos)
help(Stripe)
# Checkout.imprimir_lista(lista_productos)
# print(checkout.obtener_total(lista_productos))
