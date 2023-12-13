suma=0
a = input("Introdueix un número: ")
#Bucle cada digit en la cadena se suma 
for i in a:
	suma = suma + int(i)
print("La suma dels dígits del número {} és {}".format(a,suma))
# Comprova si és par la suma o imparell dels dígits 

if suma%2==0:
	print("La suma dels dígits del número {} és parell".format(a))
else:
	print("La suma dels dígits del número {} és senar".format(a))
