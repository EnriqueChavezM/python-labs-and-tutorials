"""
Primer ejemplo
    Escribir un programa que reciba una entrada en un número float
    Usar un bucle while para dividir la entrada entre 2 mientras el numero sea mayor o igual a  3.5
    imprimir el primer número que sea menor que 3.5

#Pedir numero a usuario
numero = float(input("Ingrese un numero: "))

#Ciclo
while numero >= 3.5:
    numero /= 2
print(numero)
"""

"""
Segundo ejemplo
    Escribir un programa que cuente de 1 hasta donde el usuario elija

#Pedir numero a usuario
num = float(input("Ingrese un numero hasta donde contar: "))
contador = 1
#Ciclo
while contador <= num:
    print("contador = ", contador)
    contador += 1
"""

"""
Tercer ejemplo
    Calculadora de Indise de Masa Corporal(IMC)
"""

print("Calculadora de IMC")
contador = 0

while contador !=  2:
    contador = int(input("¿Quieres Seguir Calculando el IMC?\n 1 =  SI y 2 = NO \n → "))

    if contador == 1:

        estatura = float(input("Ingrese su estatura en metros: "))
        peso = float(input("Ingrese su peso en kilogramos: "))
        resultado = round(peso / (estatura ** 2), 2)

        if resultado < 18.5:
            print(f"IMC de {resultado} = BAJO DE PESO")
        elif resultado < 24.99:
            print(f"IMC de {resultado} = PESO NORMAL")
        elif resultado < 30:
            print(f"IMC de {resultado} = SOBREPESO")
        else:
            print(f"IMC de {resultado} = OBESIDAD")

    else:
        print("Hasta pronto")
print("Gracias por utlizar la calculadora de IMC")

