def contar_digitos(numero):
    digitos = 0
    for n in str(numero):
        digitos += 1
    return digitos

a = int(input("Introdueix un número natural (<900000): "))
if a > 900000:
    print("El número és més gran que 900000. Introdueixi un número vàlid.")
else:
    print("{} té {} dígits".format(a, contar_digitos(a)))
