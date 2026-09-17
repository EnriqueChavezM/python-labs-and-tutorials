"""*****************************************************************************************
Desafío:

imprimir una n - pirámide usando *

******************************************************************************************"""

#Entrada de usuario
n = int(input())
row = 0
col = []
for i in range(1,n+1):
    if i % 2 == 0:
        continue
    else:
        row += 1        #Numero maximo de numeros inpares 0 a n (filas)
        col.append(i)   #Todos los numeros impares de 0 a n (columnas)

#Bucle imprimir triangulo
for x in range (0, row):
    r = "*"*(col[x])    #Multiplicar * x numero  impar de laposicion x 
    print(r)