"""
Crea una función que modifique una lista reemplazando un elemento por un nuevo valor.

"""
def change_element(lst, index, new_element):
    # Escribe el código aquí
    lst[index] = new_element
    print(lst)

lista = input("Ingrese una lista de elementos separados por comas: ").split(",")
index = int(input("Ingrese el índice del elemento que desea reemplazar: "))
new_element = input("Ingrese el nuevo elemento: ")
change_element(lista, index, new_element)
