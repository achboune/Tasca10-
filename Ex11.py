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
        number_1 = int(input('Please enter the first number: '))
        number_2 = int(input('Please enter the second number: '))
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
           

def calculadora_reals():
    print("Calculadora de reals")

def menu_principal():
    x = 1
    while x>0:
        print("""
            menu_principal:
                1. Calculadora enteros
                2. Calculadora reales
                3. salida
            """)
        x = int(input("Elige la opción: "))
        if x>0 and x<4:
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
        p=-1
        print("Sortir")
    else:
        print("Opció no vàlida")
   
#Inicia Calculadora de enteros (si presionas el 1 en el Menú)




   