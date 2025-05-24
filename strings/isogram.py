def is_isogram(string):
    #convertimos la cadena a minusculas y quitamos guiones y espacios
    palabra = string.lower().replace("-", "").replace(" ","")
    # si la longitud del set es igual a la longitud de la palabra retorna True
    return len(set(palabra)) == len(palabra)

print(is_isogram("Emily Jung Schw-artzkopf"))