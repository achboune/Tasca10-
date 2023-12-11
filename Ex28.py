def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal

# Solicitar al usuario que ingrese un valor binario como cadena
binary_input = input("Introduce un valor binario: ")

# Convertir la cadena binaria a decimal utilizando la función
decimal_result = binary_to_decimal(binary_input)

# Mostrar el resultado
print(f"El número binario {binary_input} en decimal es: {decimal_result}")




def bintoodec():
    return int(num,2)


