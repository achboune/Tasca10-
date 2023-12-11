def paraula_mes_llarga(lista):
    max = lista[0]
    for x in lista:
        if len(x) > len(max):
            max = x
    return max



lista = ["Hola", "Ramis", "IES", "Paraula"]
m = paraula_mes_llarga(lista)
print(m)