#Suma de llista 
def sumar_llista(llista):
    suma = 0
    for valor in llista:
        suma += valor
    return suma 
exemple_llista = sumar_llista([2, 3, 5, 6])
print(f"Suma: {exemple_llista}")






# Multiplicació llista
def multiplicar_llista(llista):
    producte = 1
    for valor in llista:
        producte *= valor 
    return producte 
exemple_llista = multiplicar_llista([3, 5, 2, 7])
print(f"Multiplicació: {exemple_llista}")