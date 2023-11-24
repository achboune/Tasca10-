def verificació_de_numero(llista, numero):
        return numero in llista 

#Exemple de ús 
mi_llista = [2, 4, 12, 8]
numero_verificar= 4

resultado = verificació_de_numero(mi_llista, numero_verificar)

print(resultado) #Imprimira True ja que el 4 surt en la mi_llista