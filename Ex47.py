def esta_ordenada(a):
    # Crear copias de la lista para comparar en orden ascendente y descendente
    b = a.copy()
    c = a.copy()

    # Ordenar las copias
    b.sort()
    c.sort(reverse=True)

    # Verificar si la lista original es igual a la lista ordenada de manera ascendente o descendente
    if a == b:
        print("La lista {} está ordenada ascendentemente {}".format(a, b))
    elif a == c:
        print("La lista {} está ordenada descendentemente {}".format(a, c))
    else:
        print("La lista {} no está ordenada {}".format(a, a))

def llegir_llista():
    # Inicializar una lista vacía
    a = []

    # Bucle de entrada hasta que se ingrese un punto (.)
    c = "a"
    while c != ".":
        c = input("Introduce un elemento de la lista y un punto (.) para finalizar: ")
        
        # Agregar la entrada a la lista si no es un punto
        if c != ".":
            a.append(c)

    return a

# Ejemplo de uso:
llista = llegir_llista()
esta_ordenada(llista)
