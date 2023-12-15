#Defenció 
def suma_entre_dos_numeros(a, b):
    total = sum(range(a, b+1))
    return total
2
# Demanem a l'usuari que introdueixi dos números
a = int(input("Introdueixi el primer número: "))
b = int(input("Introdueixi el segon número: "))

# Calculem la suma utilitzant la funció i mostrem el resultat
resultat = suma_entre_dos_numeros(a, b)
print("La suma de tots els números entre {} i {} és {}".format(a, b, resultat))
