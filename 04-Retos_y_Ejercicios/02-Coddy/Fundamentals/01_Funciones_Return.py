"""
Tema: Funciones / Return
Ejercicio: 
    1. Crea una función llamada `square_number` que reciba un único parámetro `n` y devuelva su cuadrado (n × n).
    2. Crea una variable llamada `input_num` que reciba la entrada del usuario (conviértela a entero usando `int()`).
    3. Llama a la función con `input_num` como argumento y guarda el valor devuelto en una variable llamada `result`.
    4. Finalmente, imprime `result`.
"""
def square_number(n):
    return n * n

def input_num():
    x =square_number(int(input("Ingrese un numero:\n→ ")))
    return x
result = input_num()
print(result)