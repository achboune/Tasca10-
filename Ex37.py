def verificar_rima(x, y):
    if x[-3:] == y[-3:]:
        return "en las últimas tres letras"
    elif x[-2:] == y[-2:]:
        return "en las últimas dos letras"
    elif x[-1:] == y[-1:]:
        return "en la última letra"
    else:
        return "no"

x = input("Introduce la primera palabra: ")
y = input("Introduce la segunda palabra: ")

rima_resultado = verificar_rima(x, y)
if rima_resultado != "no":
    print("Las palabras {} y {} riman {}".format(x, y, rima_resultado))
else:
    print("Las palabras {} y {} no riman.".format(x, y))
