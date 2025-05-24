"""def translate(text):
    vocales= ['a','e','i','o','u']
    consonantes =[]
    lista = list(text)
    if text[0] in vocales or text[:2] == "xr" or text[:2] == "yt":
        return text + "ay"
    i = 0
    while i < len(text) and (text[i] not in vocales and text[i] != 'y'):
        if text[i:i+2] == "qu":
            consonantes.append(text[i:i+2])
            i += 2
        else:
            consonantes.append(text[i])
            i += 1
    nueva_cadena = text[i:] + "".join(consonantes) + "ay"
    return nueva_cadena"""


def translate(text):
    vocales = ['a', 'e', 'i', 'o', 'u']
    consonantes = []

    # Caso 1: Comienza con vocal, "xr" o "yt"
    if text[0] in vocales or text[:2] in ["xr", "yt"]:
        return text + "ay"

    # Caso 2: Comienza con consonantes
    i = 0
    while i < len(text) and (text[i] not in vocales and text[i] != 'y'):
        # Manejo de "qu"
        if text[i:i+2] == "qu":
            consonantes.append(text[i:i+2])
            i += 2
        else:
            consonantes.append(text[i])
            i += 1

    # Construye la nueva cadena
    nueva_cadena = text[i:] + "".join(consonantes) + "ay"
    return nueva_cadena

print(translate("yellow"))