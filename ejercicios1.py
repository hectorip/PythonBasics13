# -*- coding: utf-8 -*-

# Una función que calcule los primeros 20 números primos.

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
    return primos

print(primeros_20_primos())

# función que calcula n primos

def primeros_n_primos(n):
    if not n:
        return []
    primos = [2]
    contador = 3
    while(len(primos) < n):
        es_primo = True
        for primo in primos:
            if contador % primo == 0:
                es_primo = False
                break;
        if es_primo:
            primos.append(contador)
        contador += 2;

    return primos

print(primeros_n_primos(1000))


# hacer slug una cadena de texto

def slug(frase):
    reemplazos = {
        " ": "_",
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "ñ": "n"
    }
    frase = frase.strip()
    frase = frase.lower()

    for v, n in reemplazos.iteritems():
        frase = frase.replace(v, n)

    return frase

print(slug("20 cosas que no sabías de un programador"))


# encontrar anagramas de una palabra
# recursividad

def obtener_anagramas(palabra):
    if len(palabra) == 1:
        return list(palabra)

    letras = list(palabra)
    unique_letras = list(set(letras))
    anagramas = []
    for letra in unique_letras:
        n_lista = letras[:]
        n_lista.remove(letra)
        # TODO: eliminar duplicados
        for anagrama in obtener_anagramas(n_lista):
            anagramas.append(letra + anagrama)
    return anagramas

# singulait = obtener_anagramas("singularit")
print(len(singulait))
