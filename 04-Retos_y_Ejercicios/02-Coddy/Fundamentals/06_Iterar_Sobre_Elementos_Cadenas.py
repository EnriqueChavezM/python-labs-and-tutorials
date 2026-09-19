"""*****************************************************************************************

Crear un programa que reciba una lista como entrada, e imprima una nueva lista que contenga solo las palabras mas largas que 5 caracteres

*****************************************************************************************"""

"""lista = input("ingrese una lista de palabras separadas por comas: ").split(",")
nueva_lista = [palabra for palabra in lista if len(palabra) > 5]
print("Las palabras con más de 5 caracteres son:", nueva_lista)
"""

"""*****************************************************************************************

Crea un programa que reciba una cadena de texto como entrada e imprima cuántas veces aparece el carácter "p" (o "P") en ella.

*****************************************************************************************"""

"""text = input("Ingrese una cadena de texto:\n→ ").lower()
caracter = input("Ingrese caracter a contar:\n→ ").lower()

# opcion 1
conteo = [char for char in text if char == caracter]
print(len(conteo))

# opcion 2
cont = 0
for char in text:
    if char == caracter:
        cont += 1
    else:
        continue
print(cont)"""

"""*****************************************************************************************

Escribe un programa que reciba dos entradas: 
 - Una cadena de texto y un carácter delimitador. 
 - El programa deberá dividir el texto por espacios en blanco en palabras
 - Luego unir estas palabras usando el carácter delimitador especificado e imprimir la cadena resultante.

*****************************************************************************************"""

"""text = input("Ingrese una cadena de texto:\n→ ").split()
delimitador = input("Ingrese caracter delimitador:\n→ ")

print(f"Texto resultante: {delimitador.join(text)}")"""

"""*****************************************************************************************

Escribe un programa que reciba dos entradas: 
 - Una cadena de números separados por espacios, una cadena de prefijo.
 - El programa debe dividir la cadena de números en números individuales,
 - Agregar el prefijo a cada número.
 - Luego unir estos números modificados de nuevo en una sola cadena separada por espacios
 - Finalmente, imprimir la cadena

*****************************************************************************************"""

numeros = input("Ingrese cadena de numeros separados por espacios:\n→ ").split()
prefijo = input("Ingrese el prefijo:\n→ ")
lista_resultante = []
for num in numeros:
    lista_resultante.append(prefijo + num)
cadena_final = " ".join(lista_resultante)
print(cadena_final)
