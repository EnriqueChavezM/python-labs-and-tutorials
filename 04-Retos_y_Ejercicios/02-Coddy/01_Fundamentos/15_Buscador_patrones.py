"""*****************************************************************************************

Desafío:

Crea una función llamada find_occurrences que:
    1. Tome dos argumentos de cadena: text y pattern
    2. Cuente cuántas veces aparece pattern en text, incluyendo ocurrencias superpuestas
    3. Devuelva una tupla que contenga:
        3.1 Un booleano que indique si se encontró el patrón (True/False)
        3.2 El número de ocurrencias del patrón
        3.3 Una lista de las posiciones iniciales donde se encontró el patrón

*******************************************************************************************"""
def find_occurrences(text, pattern):

    # Escribe tu código aquí
    conteo = 0
    posisiones =  []
    b_ocurrencias = False

    for i in range(len(text)):

        #Verificar coinsidencia de muestra con patron
        if text[i:i+len(pattern)] == pattern:
            conteo += 1             # Conteo de ocurrencias
            posisiones.append(i)    # Agregar Posicion de ocurrencias a lista  
            b_ocurrencias = True     # Cambiar estado de bandera de ocurrencias
            
    resultado = (b_ocurrencias,conteo,posisiones) #Crear tupla de resultados
    return resultado

# Leer entrada
text = input("Ingrese Cadena de texto:\n→ ")
pattern = input("Ingrese Patron a Buscar:\n→ ")

# Llama a tu función e imprime el resultado

print(f"Resultado:\n{find_occurrences(text, pattern)}")