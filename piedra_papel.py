# Eleccion aleatoria maq
import random

# function randint(min,max)
rand_int=random.randint(1,3)
if rand_int==1:
    choice_maq="PIEDRA"
elif rand_int==2:
    choice_maq="PAPEL"
else:
    choice_maq="TIJERAS"



#Eleccion de usuario
choice_text='''
Escribe una de las opciones:
    PIEDRA 
    PAPEL
    TIJERAS
'''
choice_user=input (choice_text)
#impresion de opciones

print ("Usuario eligio ->", choice_user)
print ("Maquina eligio ->", choice_maq)

#ganador
if choice_maq==choice_user:
    print("Empate")
else:
    if choice_maq=="PIEDRA" and choice_user=="PAPEL":
        print("Gana Usuario")
    elif choice_maq=="PIEDRA" and choice_user=="TIJERAS":
        print("Gana Maquina")
    elif choice_maq=="PAPEL" and choice_user=="TIJERAS":
        print("Gana Usuario")
    elif choice_maq=="PAPEL" and choice_user=="PIEDRA":
        print("Gana Maquina")
    elif choice_maq=="TIJERAS" and choice_user=="PIEDRA":
        print("Gana usuario")
    else:
        print("Gana Maquina")
        
    