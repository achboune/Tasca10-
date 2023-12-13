# Función para verificar 
def esta_ordenada(a):
    b = a.copy()
    c = a.copy()
    
    # Ordenar la lista 
    b.sort()
    c.sort(reverse=True)
    
    # Verificar si la lista original 
    if a == b:
        print("La lista {} está ordenada ascendentemente {}".format(a, b))
    elif a == c:
        print("La lista {} está ordenada descendentemente {}".format(a, c))
    # Si no cumple las condiciones, la lista no está ordenada
    else:
        print("La lista {} no está ordenada {}".format(a, b))

# Función para leer una lista de elementos
def llegir_llista():
    a = []
    c = "a"
    
    # Pedir que introduzca un punto para terminar la funcion 
    while c != ".":
        c = input("Introduce un elemento de la lista y un punto (.) para terminar: ")
        
        # Si el usuario no ingresó un punto, agregar el elemento a la lista
        if c != ".":
            a.append(c)
    
    return a

# Ejemplo de uso
mi_lista = llegir_llista()
esta_ordenada(mi_lista)
