def gran_llista(lista):
    max = lista[0]
    for x in lista:
        if x > max:
            max = x
    return max



lista = [3, 4, 2, 3, 10]
m = gran_llista(lista)
print(m)