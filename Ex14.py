#Definició de la funció 
def gra(x , y ,z):
    if x>y>z:
        print("El número {} és el major".format(x))
    elif y>x>z:
        print("El número {} és el major".format(y))
    else:
        print("El número {} és el major".format(z))
    
#Programació de la funció 
x= int(input("Introduce el primer número: "))
y= int(input("Introduce el segundo número: "))
z = int(input("Introduce el tercer núemro: "))
gra(x,y,z)
