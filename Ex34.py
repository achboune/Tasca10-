def es_de_traspas(any):
    if any % 4 == 0:
        if any % 100 != 0 or any % 400 == 0:
            return True
    return False
resultat = int(input("Introdueix un any: "))
print(es_de_traspas(resultat))