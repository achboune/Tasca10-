def mostrar_majors_que(t, x):
    for e in t:
        if e > x: 
            print(e, "és major que", x)

# Prova de la funció
t = (20, 40, 9, 17, 29)
x = 18
mostrar_majors_que(t, x)
