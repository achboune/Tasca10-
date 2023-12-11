def majuscules(cadena):
    return sum(1 for c in cadena if c.isupper())

# Ejemplos de uso
cadena1 = "Hola Mundo"
resultado1 = majuscules(cadena1)
print(f"En la cadena '{cadena1}' hay {resultado1} letras mayúsculas.")

cadena2 = "Python es divertido"
resultado2 = majuscules(cadena2)
print(f"En la cadena '{cadena2}' hay {resultado2} letras mayúsculas.")
