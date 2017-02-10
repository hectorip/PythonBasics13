# -*- coding: utf-8 -*-

def es_primo(n):
    # saber si es divisible entre algún numero que no sea 1 o sí mismo
    # n= 5
    lista_numeros_menores = range(2, n) # 2, 3, 4,

    for numero in lista_numeros_menores:
        if n % numero == 0:
            return False
    return True


print(es_primo(10))
print(es_primo(11))
print(es_primo(37))
print(es_primo(20))
