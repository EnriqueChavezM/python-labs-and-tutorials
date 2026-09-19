"""****************************************************************************************

Crea un programa que reciba dos listas e imprima una nueva lista con todos los elementos que están en la primera lista pero NO en la segunda.

****************************************************************************************"""
"""# Divide cada cadena de entrada en una lista, usando comas como separadores
lst1 = input("Ingrese la primer lista separada por comas:\n→ ").split(",")
lst2 = input("Ingrese la segunda lista separada por comas:\n→ ").split(",")
# Escribe tu código a continuación
lst3 = []
for l in lst1:
    if l not in lst2:
        lst3.append(l)

print(f"Lista resultante:\n{lst3}")"""

"""****************************************************************************************

Crea una función llamada not_mutual_friends que tome dos listas de nombres que representen las listas de amigos de dos personas.
La función debe devolver una lista de nombres que sean amigos de solo una persona (no amigos en común).

Supongamos que tenemos:

    - Amigos de la persona A: ["John", "Emma", "Mike", "Sarah"]
    - Amigos de la persona B: ["Emma", "Tom", "Sarah", "Peter"]
    - Cuando llamemos a not_mutual_friends con estas dos listas, debería devolver: ["John", "Mike", "Tom", "Peter"]

Explicación:

    - "John" y "Mike" solo son amigos de la persona A
    - "Tom" y "Peter" solo son amigos de la persona B
    - "Emma" y "Sarah" son amigos en común (amigos de ambas personas), por lo que no se incluyen en el resultado

****************************************************************************************"""
def not_mutual_friends(list1, list2):
    # Escribe tu código debajo
    lista = []
    for x in list1:
        if x not in list2:
            lista.append(x)
    for y in list2:
        if y not in list1:
            lista.append(y)
    return lista

lst1 = input("Ingrese la primer lista de nombres separada por comas:\n→ ").split(",")
lst2 = input("Ingrese la segunda lista de nombres separada por comas:\n→ ").split(",")

print(f"Listas de nombres nocomunes:\n {not_mutual_friends(lst1,lst2)}")