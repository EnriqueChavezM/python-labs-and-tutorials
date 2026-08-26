"""
Primer ejemplo
    Escribe código que imprima un patrón rectangular de estrellas (*) usando bucles anidados.

    El programa debe:
        -Leer dos números enteros: filas y columnas.
        -Usar una estructura de bucles anidados para imprimir el patrón.
        -El bucle exterior debe iterar sobre cada fila.
        -El bucle interior debe construir cada fila con la cantidad correcta de estrellas.
        -Imprimir cada fila completada.
    Ejemplo: 
        Si la entrada es de 3 filas y 4 columnas, la salida debe ser:
        ****
        ****
        ****

#Obtener Numero de filas y columnas
row = int(input("Ingrese numero de filas: "))
col = int(input("Ingrese numero de columnas: "))

#Bucle externo para filas
for x in range (0, row):
    r = ""
    #Bucle interno para columnas
    for y in range(0, col):
        r += "*"
    print(r)

"""

"""
Segundo ejemplo
    Escribe un programa que encuentre todos los pares de números del 1 al n (inclusive) que, al multiplicarse, den como resultado n.
    El programa debe mostrar todas las combinaciones posibles, incluyendo pares duplicados en orden inverso. 
    Por ejemplo, se deben mostrar tanto "1 x 6" como "6 x 1", ya que se consideran diferentes combinaciones del mismo par. Los números también pueden emparejarse consigo mismos si su producto es igual a n.

    Importante: Solo se consideran números del 1 al n. Si n es menor que 1, no existen pares.

"""
n = int(input("Ingrese un numero \n"))
for i in range (1, n+1):
    for j in range (1, n+1):
        result = i * j
        if result == n:
            print (f"{i} x {j} = {n}")