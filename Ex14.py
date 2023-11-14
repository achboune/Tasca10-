#Definició de la funció 
def gra(x , y ,z):
    if x>y>z:
        print(x)
    elif y>x>z:
        print(y)
    else:
        print(z)
    
#Programació de la funció 
x= int(input("Introduce el primer número: "))
y= int(input("Introduce el segundo número: "))
z = int(input("Introduce el tercer núemro: "))
gra(x,y,z)