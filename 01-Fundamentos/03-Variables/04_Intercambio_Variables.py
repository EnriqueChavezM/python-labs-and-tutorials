"""******************************************************************************************

Desafío

Escribe un programa para intercambiar los valores de dos variables sin utilizar una variable temporal. 
    - Inicializa dos variables, x e y, con los valores 5 y 10 respectivamente. 
    - Intercambia sus valores y luego imprímelos.

*******************************************************************************************"""
# Inicializar las variables x e y
x = 5
y = 10
print(f"valor de x inicial: {x}")
print(f"valor de y inicial: {y}\n")
# Intercambiar los valores de x e y
x,y = y,x

# Imprimir los valores intercambiados
print(f"valor de x final: {x}")
print(f"valor de y final: {y}")