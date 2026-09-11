"""*****************************************************************************************

Crea una función que reciba dos argumentos: 
    1. Una lista de números. 
    2. Un número entero. 

La función debe: 
    1. Concatenar la lista consigo misma (list + list)
    2. Repetir la lista resultante 
    3. Devolver el patrón final.

*****************************************************************************************"""

"""def crear_patron(numeros, repetir):
    
    lista = numeros + numeros
    lista2 = lista  * repetir
    return lista2

num = input("Ingrese lista de numeros separad por comas:\n→ ").split(",")
rep = int(input("Ingrese el numero de veces a repetir:\n→ "))

print(crear_patron(num, rep))"""

"""*****************************************************************************************

Crea un programa que reciba una lista de números como entrada e imprima una nueva lista que:
    → Contenga la lista original seguida de su inversa 
    → Tenga el primer elemento de la lista original insertado al principio y el último elemento insertado al final
    → Repita toda esta secuencia dos veces.

*****************************************************************************************"""

numbers = input("Ingrese lista de numeros separad por comas:\n→ ").split(",")
# Escribe tu código debajo
lista = []
lista.append(numbers[0])
lista = lista + numbers
listaR = numbers[::-1]
lista = lista + listaR
lista.append(numbers[-1])
lista *= 2
print(lista)
