"""*****************************************************************************************

Crea un programa que reciba una lista como entrada e imprima la siguiente lista segmentada: 
    → Para listas de longitud impar: 
        → Toma el elemento central y un elemento de cada lado (3 elementos en total) 
    → Para listas de longitud par: 
        → Toma los dos elementos centrales.
        
*****************************************************************************************"""

"""lista = input("Ingrese una lista separada por comas:\n→ ").split(",")

x = len(lista)
if x % 2 != 0:
    x //= 2
    print(lista[x-1 : x+2])
else:
    x //= 2
    print(lista[x-1 : x+1])"""

"""*****************************************************************************************

Crea un programa que reciba una lista como entrada e imprima tres listas nuevas
    → Basadas en las siguientes operaciones de segmentación: 
        → Una lista que contenga cada cuarto elemento, comenzando desde el índice 2. 
        → Una lista que contenga todos los elementos desde el tercer elemento hasta el antepenúltimo.
        → Una lista que contenga cada segundo elemento en orden inverso, comenzando con el último.
        → Una lista que contenga los tres primeros y los tres últimos elementos de la lista original. 
    →Nombra las listas lista1, lista2, lista3 y lista4, respectivamente.

*****************************************************************************************"""

original_list = input("Ingrese una lista separada por comas:\n→ ").split(',')
# Escribe tu código debajo
list1 = original_list[2::4]
list2 = original_list[2:-2]
list3 = original_list[::-2]
x = len(original_list)
list4 = original_list[:3] + original_list[-3:]

# No cambies nada debajo de esta línea
print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)
print("List 4:", list4)