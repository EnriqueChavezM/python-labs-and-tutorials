"""
Primer Ejemplo (Funsion Simple)
    Escribe un programa que reciba un único dato de entrada, un número n.
    Crea una función llamada print_large_number que imprima el número 50005000. 
    Luego, llama a esa función n veces usando un bucle for, de modo que el número se imprima n veces en total. 

#Declarar funcion
def print_large_number():
    print (50005000)

n =  int(input("Cuantas veces se imprimira: \n→ "))
for i in range(n):
    #Llamar funcion
    print_large_number()
    
"""

"""
Segundo ejemplo (Funcion con argumento)
    Escribir funcion que reciva un numero y muestre si es  par o impar


def es_par(numero):
    if numero % 2 == 0:
        print(f'El número {numero} es par')
    else:
        print(f'El número {numero} es impar')

for i in range(15,34):
    es_par(i)
print("---------")
for i in range(50,95):
    es_par(i)

"""

"""
Tercer ejemplo
    Escrivir funcion reste 2 numeros
    Si no tiene numero o falta alguno deve mandar un error 
    Inicialisar los parametros de la  funcion para evitar errores de conpilacion
"""
def resta (a = None, b = None):
    if a  == None or b == None:
        print("Error, debes enviar 2 numeros a la funcion")
        return
    return a - b
#Manda el error
resta() 
resta(1)
#Realisa la resta
resultado = resta(5,2) 
print(resultado)
