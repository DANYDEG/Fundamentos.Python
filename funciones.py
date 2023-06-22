# Funciones en Python 
# def name_function(params):
#   Codigo 
#   return

# funcion sin parametros y sin retornos
def saludos():
    print("Hola a todos")

saludos()

#funciones con un parametro 
def get_age_in_future(age):
    print(f"en 3 años tendras {age+3} años")

get_age_in_future(19)

# funciones con 2 parametros sin retorno
def suma(num1, num2):
    print(f"{num1}+{num2}={num1 + num2 }")

    suma (12,35)

# funciones con paramentros opcionales 

def get_heroes(h1="Ironman", h2="spiderma"):
    print([h1,h2])

    get_heroes()
    get_heroes("batman")
    get_heroes("batman", "superman")
    get_heroes(h2="batman", h1="superman")

    # fuunciones de retorno

def title(texto):
    return texto.title()

text_changed=title("Hola a todos")
print (text_changed)