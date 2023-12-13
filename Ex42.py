#Definicio de la funció 
def taula_multiplicar(a):
      #Bucle que va del 1 al 20 
	for i in range(20):
             #Imprimeix la multiplicació 
            print("{} x {} = {}".format(i+1, a, (i+1)*a))
#Pprincipal
x = int(input("Introdueixi un número per a calcular la seva taula de multiplicar: "))
taula_multiplicar(x)


