def nums_que_comencen_per(llista, lletra):
    contador = 0

    for nom in llista:
        if nom.lower().startswith(lletra.lower()):
            contador += 1
    return contador

#Ejemplo 
noms = ['Ana', 'Juan', 'Marta', 'Alberto']

# Pedir una letra al usuario
lletra = input("Introduce una letra: ")

# Llamar a la función con la lista y la letra introducida por el usuario
resultado = nums_que_comencen_per(noms, lletra)

# Imprimir el resultado
print(f"La cantidad de nombres que comienzan con '{lletra}' es: {resultado}")
