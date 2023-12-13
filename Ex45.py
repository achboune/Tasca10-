#Definició
def eliminar_capicua(llista):
    if len(llista) > 1:
        return llista[1:-1]
    else:
        return []

# Exemple 
llista = [1, 2, 3, 4, 5]
print(eliminar_capicua(llista))  # Això imprimirà: [2, 3, 4]
