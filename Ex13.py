#Definició de la funció 
def gra(x , y):
    if x>y:
        return print(x)
    else:
        return print(y)
#Programació de la funció 
x= float(input("Introduce el primer número: "))
y= float(input("Introduce el segundo número: "))
gra(x,y)