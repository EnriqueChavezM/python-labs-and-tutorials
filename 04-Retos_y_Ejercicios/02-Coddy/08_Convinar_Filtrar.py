"""
Crea una funcion que reciba 2 argumentos:
    - Elprimer argumento en una lista de númerios
    - El segundo argumento es un valor entero de umbral

La funcion debe:
    1. Elimina todos los numeros que sean menopres o igual al valor de umbral
    2. Ordenar los números restantes en orden asendente.
    3. Devolver la lista resultante. 
    """
def combinar_filtrar(lista_numeros, umbral):
    # Filtrar los números mayores al umbral
    numeros_filtrados = [num for num in lista_numeros if num > umbral]
    """
    similar a 
    numeros_filtrados = []
    for i in lista_numeros:
        if i > umbral:
            numeros_filtrados.append(i)
    """
    # Ordenar la lista resultante en orden ascendente
    numeros_filtrados.sort()
    
    return numeros_filtrados

#Pedir numeros al usuario
entrada = list(map(int, input("Ingrese una lista de numeros separados por comas: ").split(",")))
umbral = int(input("ingrese el umbral: "))

# llamar la funcion
print(f"lista resultante: {combinar_filtrar(entrada, umbral)}")
