def llegir_llista():
    result_list = []
    a = '1'
    while a != ".":
        a = input("Introduce el siguiente parametro: ")
        if a != ".":
            result_list.append(a)
    return result_list

def filter_llista(o, s):
    p = []
    for e in o:
        if len(e) > s:
            p.append(e)
    return p

l = llegir_llista()
t = int(input("Introduce el tamaño de la lista: "))
print(filter_llista(l, t))
