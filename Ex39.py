x = int(input("Introdueixi un número natural (<100): "))

if x > 100:
    print("El número és més gran que 100. Introdueixi un número vàlid.")
else:
    suma = 0
    for i in range(x, 1, -4):
        suma += i**2

    print("La suma dels quadrats de 4 posicions menys de {} és {} ".format(x, suma))
