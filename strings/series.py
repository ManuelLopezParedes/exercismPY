def slices(series, length):
    """
    Dada una cadena de dígitos, 
    genere todas las subcadenas contiguas de longitud n
    en esa cadena en el orden en que aparecen
    ej. "49142"
    salida si lenght es 3 "491", "914", "142"
    salida si lenght es 4 "4914", "9142"
    """
    # manejo de errores
    if length == 0: # si lenght es 0
        raise ValueError("slice length cannot be zero")
    
    elif length < 0: # si lenght es negativo
        raise ValueError("slice length cannot be negative")
    
    elif not series: # si series esta vacio
        raise ValueError("series cannot be empty")
    
    elif length > len(series): # si lenght es mayor que series
        raise ValueError("slice length cannot be greater than series length")
    
    else: # si no hay error ejecuta el siguente codigo
        lista = [] # creamos la lista que retornaremos
        cadena = "" # cadena que nos ayudara a guardar los valores
        ser = str(series) # convertimos series en un string

        for i in range(len(ser) - length + 1): # definimos el numero de iteraciones
            cadena += ser[i:i+length] # sumamos a cadena los valores correpondientes
            lista.append(cadena) # agregamos esos valores como un elemento de lista 
            cadena = "" # limpiamos la cadena
    return lista # regresamos lista


print(slices(49142,3))