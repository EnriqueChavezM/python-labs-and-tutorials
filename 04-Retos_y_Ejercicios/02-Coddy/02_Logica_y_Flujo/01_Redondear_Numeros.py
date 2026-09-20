"""******************************************************************************************

Desafío

Escribe un programa que reciba dos entradas independientes del usuario y muestre el resultado redondeado:
    1. La primera entrada debe ser un número (flotante). 
    2. La segunda entrada debe ser el número de posiciones decimales al que se debe redondear (entero).

Ejemplo:
    Si las entradas son 3.14159 y 2, el programa debería mostrar 3.14.

*******************************************************************************************"""
# Toma una entrada float del usuario
numero = float(input("Ingrese un numero con punto decimal:\n→\t"))

# Toma una entrada entera del usuario para el número de decimales
redondeo = int(input("Ingrese a  cuantos decimales desea redondear el  numero:\n→\t"))

# Imprime el número redondeado
print(round(numero,redondeo)) 