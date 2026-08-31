"""
Primer Ejemplo (break)
    Escribe un programa que:
        1. Tome 2 numeros como entrada
        2. Itere a través del rango de números eseable la primera entrada hasta la segunda entrada (sin incluir el segundo)
        3. Encuentre e imprime el primer número par mayor que 5
        4. Luego, en un bucle separado, encuentre e imprima el primer número divisible por 7
    

#Pedir numeros al usuario
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

#Bucle
for i in range(num1, num2):
    if i > 5 and i % 2 == 0:
        print(f"El primer número par mayor que 5: {i}")
        break

for i in range(num1, num2):
    if i % 7 == 0:
        print(f"El primer numero divisible entre 7: {i}")
        break
"""

"""
Segundo ejemplo (continue)
    Se te proporciona un código que imprime los números del 1 al 100 (inclusive).
        for i in range(1, 101):
            print(i)
    Tu tarea consiste en añadir sentencias `if` y `continue` para que se impriman todos los números excepto los múltiplos de 3. En otras palabras, omite cualquier número divisible por 3.
    Por ejemplo, 
        - La salida debería incluir 1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, etc., pero debería omitir 3, 6, 9, 12, 15, 18, etc.
"""
for i in range(1, 101):
    if i % 3 == 0:
        continue
    print(i)