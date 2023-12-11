def nums_que_comencen_per(llista):
    contador = 0
    for nom in llista:
        if nom.lower().startswith('a'):
            contador += 1
    return contador

# Ejemplo de uso:
noms = ['Anna', 'Albert', 'Bernat', 'Carla', 'Antoni']
print(nums_que_comencen_per(noms))  # Esto imprimirá 3
