"""
Tema: Resumen - Función Sigma
Ejercicio: 
    1. Escribe una función llamada sigma con un argumento que represente un número n.
    2. La función devolverá la suma de todos los números del 1 al n (inclusive).

Por ejemplo:
    - Para sigma(5), la función devolverá 15, ya que 15 = 1 + 2 + 3 + 4 + 5.

Nota: 
    -El resultado debe ser un número entero: la suma de números enteros siempre es un número entero.
"""
def sigma(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma

def input_num():
    x =sigma(int(input("Ingrese un numero:\n→ ")))
    return x
result = input_num()
print(result)