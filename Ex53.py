#definició
def numeros():
    pares = []
    impares = []
#Dependencia de números parells i senars 
    for i in range(1, 101):
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    print("Els números pars del 1 al 100 son {}".format(pares))
    print("Els números senars del 1 al 100 son {}".format(impares))

numeros()
