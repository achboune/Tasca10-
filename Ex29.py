from datetime import datetime

def calcular_edad(anio_actual, anio_nacimiento):
    return anio_actual - anio_nacimiento

# Solicitar al usuario el año actual
anio_actual = int(input("Introduce el año actual: "))

# Crear una lista para almacenar la información de las personas
personas = []

# Solicitar información para cada persona
for i in range(4):
    nombre = input(f"Introduce el nombre de la persona {i + 1}: ")
    anio_nacimiento = int(input(f"Introduce el año de nacimiento de {nombre}: "))
    edad = calcular_edad(anio_actual, anio_nacimiento)
    personas.append((nombre, anio_nacimiento, edad))

# Imprimir la tabla con la información
print("\nNom\t\tData naixement\tAnys que farà aquest any")
for nombre, anio_nacimiento, edad in personas:
    print(f"{nombre}\t\t{anio_nacimiento}\t\t{edad}")

