"""
Primer ejemplo
    Escribe un programa que imprima "Hola:" y el valor de i desde 3 hasta 27 (ambos inclusive), usando un bucle for.
    Esto significa que imprimirás 25 líneas en total, comenzando en 3 y terminando en 27.

#Codigo 
for i in range (3,28):
    print("Hola:" + str(i))

"""

"""
Segundo ejemplo
    Escribe un programa que cuente la cantidad de números pares entre 10 y 50 (inclusive).
    
    Condiciones:
    - Usa un bucle `for` y una sentencia `if` para comprobar si cada número es par.
    - Almacena el resultado en una variable

evento = 0

for i in range(10,51):
    if (i % 2 == 0):
        evento += 1
    else:
        evento

print(f"En el rango de 10 a 51 el numero  depares es = {evento}.")

"""

"""
Terer ejemplo
    El factorial es una operacion matematica, el factorial de n es el producto de todos los numeros enteros positivos menores o iguales a n

    Casos especiales:
    - Factorial de 0 = 1 (por convención matemática)
    - Factorial de 1 = 1

    Escrive un programa que calcule el factorial de un numero entero dado
    IMPORTANTE: dede manejar todos los números enteros no negativos, incluyendo 0 y 1

    Recorrido ejemplo
    para entrada = 5:
    - comienza con r = 1
    - Multiplica por 1: r =  1 x 1 = 1
    - Multiplica por 2: r =  1 x 2 = 2
    - Multiplica por 3: r =  2 x 3 = 6
    - Multiplica por 4: r =  6 x 4 = 24
    - Multiplica por 5: r =  24 x 5 = 120


numero = int(input("Ingrese un numero:\n"))
resultado = 1
for i in range(1,  numero + 1):
    resultado *= i
print(f"{numero}! = {resultado}")
"""

"""
Cuarto ejemplo
    Escribe un programa aprobechando los 3 parametros de la funcion range()

    Condiciones:
    -El usuario puede decidir inicio, fin, y paso de la funcion
    -Imprimir cada numero en una linea
"""
#Pedir a usuario losparametros de la funcion
inicio = int(input("Ingrese el punto de inicio:\n"))
fin = int(input("Ingrese el punto de fin(no incluido): \n"))
paso = int(input("ingrese el paso de la funcion:\n"))

#Bucle
for i in range(inicio,fin,paso):
    print("→ " + str(i))