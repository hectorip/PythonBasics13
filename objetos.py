# -*- coding: utf-8 -*-

class Animal:
    n_patas = 4
    color = "negro"
    sonido = ""

    def hacer_sonido(self):
        print(self.sonido)

    def correr(self):
        print("run run run")


perro = Animal()
gato = Animal()
print(perro.sonido)
perro.sonido = "Gua gua!!!!"
perro.color = "amarillo"
print(perro.sonido)
perro.hacer_sonido()
# mi_diccionario.iteritems()
