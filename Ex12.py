def bintodec(N):
    a=int(N,2)
    return dectooct (a)
def bintooct(N):
    a=int(N,2)
    return oct (a)
def bintohex(N):
    a=int(N,2)
    return hex (N)

def calculadora_enters():
    y = 1
    while y>0:
        print(""""
            Calculadora de enters
                1. Sumar
                2. Resta
                3. Multiplicación
                4. División
                5. Sortir
              """)
        y = int(input("Elegeixi opció: "))
        number_1 = int(input('Introduce el primer número: '))
        number_2 = int(input('Introduce el segundo número: '))
        if y == 1: #Suma
            print('{} + {} = {}'.format(number_1, number_2,number_1+number_2))
        elif y == 2: #Resta
            print('{} - {} = {}'.format(number_1, number_2,number_1-number_2)) 
        elif y == 3: #Multipicar
            print('{} * {} ='.format(number_1, number_2), end=" ")
            print(number_1 * number_2)
 
        elif y == 4: #División
            print('{} / {} ='.format(number_1, number_2), end=" ")
            print(number_1 / number_2)
        elif y == 5: # Sortir
            y=-1
        else:
            print("Vuelve a Intentarlo: \n")

def canvis_de_base(): 
    x = 1
    while x > 0:
        print("""
            Canvis de Base 
                1.Binari 
                2.Decimal 
                3.Octal
                4.Hexadecimal
                5.Sortir
            """) 
        def canvis_de_base():
            x = 1
            while x>0:
                print("""
                Menú canis de base
                1.Donat un binari ho passem a tota la resta
                2.Donat un octal el passem a tota la resta
                3.Donat decimal ho passem a tota la resta 
                4.donat un hexadecimal ho passem ha tota la resta
                5.Sortir               
                """)
                y= int(input("Introdueix el número Binario: "))   
            if y:
                b = input("Introdueix el número bianri")
                o = bintooct(b)
                d = bintodec(b)
                h = bintohex(b)
                print("El número binari {} és: \n oct -> {} \n dec -> {} \n hex -> {}".format(b,o,d,h))
            elif 2: #Octal 
                o = input("Introdueix el número octal: ")
                b = octtobin(o)
                d = octtodec(o)
                h = octtohex(o)
                print("El número octal {} és: \n bin -> {} \n dec -> {} \n hex -> {}".format(o,b,d,h))
            elif 3: #Decimal
                d = int(input("Introdueix el número decimal"))
                b = dectobin(d)
                o = dectooct(d)
                h = dectohex(d)
                print("Introdueix decimal {} és \n bin -> {} \n oct -> {} \n hex -> {}".format(d,b,o,h))
            elif 4: #Hexadecimal
                h = input("Introdueix el número hexadecimal")
                b = hextobin(h)
                o = hextooct(h)
                d = hexttodec(h)
                print("El número hexadecimal {} és: \n bin -> {} \n oct -> {} \n dec -> {}".format(h,b,o,d))
            elif 5: #Sortir
                print("Adéu, tornaràs a la calculadora inicial \n\n")
                y=-1

        #Programa canvis de base 
        s = int(input("Elige una opción: "))
        
        if s == 1: 
            
            numero = int(input("Introduce el primer numero:\n "))
            convertido = bin(numero)
            print(convertido)
            
        elif s == 2: #Decimal
                
            numero = int(input('Introduce un número:\n'))
            convertido = bin(numero)[2:]
            print(convertido)

        
        elif s == 3: #Octal
    
            numero = int(input('Introduce un número:\n'))
            convertido = oct(numero)[2:]
            print(convertido)


        elif s == 4: #Hexadecimal
            numero = int(input('Introduce un número:\n'))
            convertido = hex(numero)[2:]
            print(convertido)

        elif s == 5: #Sortir 
            s = -1
        else:
         print("Vuelve a Interntarlo \n")




def calculadora_reals():
    print("Calculadora de reals")

def menu_principal():
    x = 1
    while x>0:
        print("""
            menu_principal:
                1. Calculadora enteros
                2. Calculadora reales
                3. Canvis de base 
                4. salida
            """)
        x = int(input("Elige la opción: "))
        if x>0 and x<5:
            return x
        else:
            print("Vuelve a Intentarlo: \n")

#Programa principal          
p = 1
while p>0:
    p = menu_principal()
    if p==1:
        calculadora_enters()
    elif p==2:
        calculadora_reals()
    elif p==3:
        canvis_de_base()
    elif p== 4:
        p=-1
        print("Sortir")
    else:
        print("Opció no vàlida")
   
#Inicia Calculadora de enteros (si presionas el 1 en el Menú)

