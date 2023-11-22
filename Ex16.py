def vocals(c):
    if c == "a" or c == "e" or c == "i" or c == "o" or c== "u":
        return True 
    elif c == "A" or c == "E" or c == "I" or c == "O" or c == "U":
        return True 
    else: 
        return False
    
    
caracter= input("Introduce un caracter: ")
print(vocals(caracter))
    