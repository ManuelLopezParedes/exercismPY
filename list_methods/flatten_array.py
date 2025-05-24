def flatten(iterable):
    lista =[]
    for item in iterable:
        if isinstance(item,int):
            lista.append(item)
        elif isinstance(item,list):
            lista.extend(flatten(item))
    return lista

print(flatten([1, [2, 3, 4, 5, 6, 7], 8]))