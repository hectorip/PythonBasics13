# -*- coding: utf-8 -*-

class MetodoDePago:
    def cobrar(self, cantidad):
        pass

class Stripe(MetodoDePago):
    """
        Esta clase es la encargada de cobrar con Stripe.
        implementa la Interfaz de Método de pago.
    """
    token = "aslkdnlaksndlkasndlkanweojhaiorwh0i3q"
    mail = "hector@checkout.com"

    @classmethod
    def cobrar(cls, cantidad):
        '''
            Esta esla función que cobra
        '''

        # hice todos los pasos necesarios para cobrar
        print("Cobré con Stripe %s" % cantidad)

    @staticmethod
    def un_metodo_statico():
        pass

class Efectivo(MetodoDePago):
    def cobrar(self, cantidad):
        print("Envíe correo al cliente para que prepare el dinero")

class Bitcoin(MetodoDePago):
    def cobrar(self, cantidad):
        print("Cobré %s bitcoins" % cantidad)
