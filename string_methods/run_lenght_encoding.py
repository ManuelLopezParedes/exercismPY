def decode(string):
    """
        de una cadena codificada regresa la cadena original
        ej 3wd2w
        salida wwwdww
    """
    cadena = ""
    num = ""
    for item in string:
        if item.isdigit(): # si item es un digito lo agrega a num como string
            num += item
        else:
            if not num: # si num esta vacia agrega el item a la cadena
                cadena += item
            else:
                cadena += item * int(num) # agrega el numero de item segun num
                num = "" # ajustamos el valor de num
    return cadena


def encode(string):
    """
        de una cadena regresa el numero de caracteres seguidos
        ej wwwdww
        salida 3wd2w
    """
    cadena = ""
    num = 0
    eval = ""

    if not string: # si la cadena esta vacia regresa la cadena vacia 
        return cadena
    
    for item in string:
        if not eval: # si eval es vacio toma el valor de item 
            eval = item
            num += 1
        else:
            if item == eval: # si el caracter anterior es igual al nuevo suma 1
                num += 1
            else: # si el caracter es diferente
                if num == 1: # si solo hay un caracter igual agrega el caracter a la cadena
                    cadena += eval
                else:
                    cadena += str(num) + eval # si hay mas agrega el numero de caracteres mas el caracter
                num = 1 # ajustamos los valores para el nuevo ciclo
                eval = item

    if num == 1: # agregamos la ultima iteracion 
        cadena += eval
    else:
        cadena += str(num) + eval
    return cadena

codigo = encode("WWDWW")
print(codigo)
print(decode(codigo))
