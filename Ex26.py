def llegir_llista():
    result_list = []
    a = '1'
    while a != ".":
        a = input("Introduce el siguiente parametro: ")
        if a != ".":
            result_list.append(a)
        else:
            return result_list

# Escoger la palabra con más caracteres
def paraula_mes_llarga(lista, p):
    max = lista[0]
    for x in lista:
        if len(x) > len(max):
            max = x
    return max

# Programa principal
l = llegir_llista()
s = int(input("Introduce el tamaño que quieres filtrar: "))  
o = paraula_mes_llarga(l, s)

print("Lista ingresada:", l)
print("Palabras con {} caracteres:".format(s), o)
