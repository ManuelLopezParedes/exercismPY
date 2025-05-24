def find(lista, value):
    cuenta = 0
    # comprobamos si la lista esta vacia 
    if not lista:
        raise ValueError("value not in array")
    
    while True:
        # conseguimos la mitad de la lista
        mitad = len(lista) // 2

        if len(lista) == 1 and lista[0] != value:
            raise ValueError("value not in array")
        
        # si encontramos el numero regresamos la cuenta +  la mitad
        elif lista[mitad] == value:
            return cuenta + mitad
        # si la mitad de la lista es mayor que el valor borramos la segunda mitad
        elif lista[mitad] > value:
            del lista[mitad:]
        # si la mitad de la lista es menor que el valor borramos la primera mitad
        elif lista[mitad] < value:
            cuenta += mitad # sumamos la mitad a la cuenta 
            del lista[:mitad]
