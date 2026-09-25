"""******************************************************************************************

Desafío 1:

1. Crea una función llamada 'frequency_counter' que tome una lista 'data_list' como argumento. 
2. La función debe contar la frecuencia de cada elemento en la lista y devolver:
    1.2. Un diccionario donde:
        1.2.1. Las claves sean los elementos únicos de la lista
        1.2.2. Los valores sean los conteos de cuántas veces aparece cada elemento.

Por ejemplo:
    - Si la lista de entrada es 
        [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    - La función debe devolver un diccionario como este:
        {1: 1, 2: 2, 3: 3, 4: 4}
*******************************************************************************************"""
print("\nDesafío: Contador de frecuencia")

def frequency_counter(data_list):
    # Escribe el código aquí 
    
    diccionario = {} #diccionario vacío para almacenar las frecuencias
    # OPCIÓN 1
    dato_anterior = None #almacenamiento de variable revisada
    for i in data_list:
        if i != dato_anterior:
            repeticiones = data_list.count(i)
            diccionario[i] = repeticiones
            dato_anterior = i
        else:
            continue

    # OPCIÓN 2 SOLUCIÓN SUGERIDA POR CODDY
    '''for item in data_list:
        if item in  diccionario:
            diccionario[item] += 1
        else:
            diccionario[item] = 1'''
            
    return diccionario

lista = list(input("Ingrese elementos de la lista separados por comas:\n→ ").split(","))
print(frequency_counter(lista))