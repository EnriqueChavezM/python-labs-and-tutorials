"""*******************************************************************************************

Ejemplo:
    1. Crea un programa que reciba un entero "score" del usuario. 
    2. El programa debe usar el operador ternario para determinar el estado basándose en el puntaje:
        2.1. Si el puntaje es mayor o igual a 50, el estado debe ser "Pass".
        2.2. Si el puntaje es menor que 50, el estado debe ser "Fail".
    3. El programa debe mostrar el estado determinado.

*******************************************************************************************"""
# Pedir puntaje de usuario
score = int(input("Ingrese el puntaje: "))

# Operación Ternaria
print("Pass" if score >= 50 else "Fail")