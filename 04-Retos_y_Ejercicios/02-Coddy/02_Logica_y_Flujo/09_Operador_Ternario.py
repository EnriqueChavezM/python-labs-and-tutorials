"""******************************************************************************************

Desafío 1:

1. Escribe un programa que tome una entrada float "temperature" que representa la temperatura actual en Celsius.
2. Usa el operador ternario para determinar un estado de advertencia basado en la temperatura:
    2.1. Si la temperatura está por encima de 30°C, la advertencia debe ser "Hot".
    2.2. Si la temperatura es 30°C o inferior, la advertencia debe ser "Normal".
3. El programa debe imprimir el estado de advertencia determinado.
*******************************************************************************************"""
temperature = float(input("Ingrese la temperatura actual en °C: "))

print("Hot" if temperature > 30 else "Normal")
