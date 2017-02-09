# -*- coding: utf-8 -*-

# Una funcion que calcule los primeros 20 números primos.

def primeros_20_primos():
    primos = [2]
    contador = 3
    while(len(primos) < 20):
        es_primo = True
        for primo in primos:
            if contador % primo == 0:
                es_primo = False
                break;
        if es_primo:
            primos.append(contador)
        contador += 2;
    print(primos)
