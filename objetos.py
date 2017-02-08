# -*- coding: utf-8 -*-

class Animal:
    n_patas = 4
    color = "negro"
    sonido = ""
    def hacer_sonido(self):
        print(self.sonido)



perro = Animal()
gato = Animal()
print(perro.sonido)
perro.sonido = "Gua gua!!!!"
perro.hacer_sonido()
# mi_diccionario.iteritems()
