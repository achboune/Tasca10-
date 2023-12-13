import random

def llista_20_elements():
    return [random.randint(1, 100) for _ in range(20)]

def hi_ha_duplicats(a):
    if len(a) != len(set(a)):
        print("La lista {} tiene elementos duplicados".format(a))
    else:
        print("La lista {} no tiene elementos duplicados".format(a))

def elimina_duplicats(a):
    return list(set(a))

# Principal
x = llista_20_elements()
hi_ha_duplicats(x)

y = elimina_duplicats(x)
y.sort()
print("La lista sin elementos duplicados es {}".format(y))
