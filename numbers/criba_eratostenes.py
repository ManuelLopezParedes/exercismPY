def criba(number):
    """
    encontrar todos los numeros primos antecesores del numero dado
    """
    if number < 1:
        raise ValueError('there is no zeroth prime')
    else:
        numeros = []
        # creacion de la lista de numeros
        for i in range(2,number+1,1):
            numeros.append(i)

    
    for num in numeros:
        res = 0
        i = 2
        # sacamos los multiplos de num hasta que sea mayor al numero dado
        while res < number:
            res = num * i
            # si el numero no esta en la lista lo ignoramos
            if res not in numeros:
                i += 1
                continue
            # si el resultado esta en la lista lo borramos
            else:
                numeros.remove(res)
                i += 1
    return numeros

print(criba(10000))