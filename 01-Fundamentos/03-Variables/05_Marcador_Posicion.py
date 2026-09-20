"""******************************************************************************************

Desafío

Escribe un programa que demuestre el uso de variables de marcador de posición en diferentes escenarios:
    - Crea un bucle que itere 5 veces. 
        -En cada iteración, imprime la palabra Iteration.
    - Tienes una lista de números: 
        - [10, 20, 30, 40, 50]. 
        - Desempaqueta esta lista en tres variables: 
            - first 
            - middle
            - last. 
        - Luego, imprime los valores de first, middle y last.

*******************************************************************************************"""
# Bucle 5 veces usando una variable de marcador de posición
for _ in range(5):
    print("Iteration")   
# Lista de números
numbers = [10, 20, 30, 40, 50]

# Desempaquetar la lista usando variables de marcador de posición
first, _, middle, _, last = numbers
# Imprimir los valores de first, middle y last
print(f"First: {first}")
print(f"Middle: {middle}")
print(f"Last: {last}")