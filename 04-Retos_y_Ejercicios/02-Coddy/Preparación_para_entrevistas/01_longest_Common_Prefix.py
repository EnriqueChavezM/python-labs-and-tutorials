"""******************************************************************************************

Desafío:

1. Recibes un arreglo de palabras strs. 
2. Devuelve la cadena más larga con la que comienzan todas las palabras. 
3. Si no todas las palabras empiezan con la misma letra, devuelve la cadena vacía "". 
4. Una palabra cuenta como prefijo de sí misma, así que una sola palabra es su propia respuesta.

Restricciones:

1 ≤ strs.length ≤ 200 
1 ≤ strs[i].length ≤ 200
Cada palabra contiene solo letras minúsculas del inglés.

Ejemplo:

Entrada
    strs = ["interview", "internet", "interval", "internal"]

Salida
    "inter"

Explicación
    Las cuatro palabras comienzan con inter. En la siguiente posición, interview y interval tienen una v, y internet e internal una n, así que el prefijo termina ahí.

*******************************************************************************************"""

def longestCommonPrefix(strs):
    primer_palabra = strs[0]

    for comparador in range(len(primer_palabra)):

        for palabra in strs[1:]:
            
            if comparador == len(palabra) or palabra[comparador] != primer_palabra[comparador]:

                return primer_palabra[ :comparador]
            
    return primer_palabra
    

lista1 = ["interview", "internet", "interval", "internal"]
lista2 = ["stack", "queue", "heap"]
lista3 = ["prefix", "pre", "prepare"]
lista4 = ["end"]

print(lista1)
print("Salida 1: " + longestCommonPrefix(lista1))

print(lista2)
print("Salida 2: " + longestCommonPrefix(lista2))

print(lista3)
print("Salida 3: " + longestCommonPrefix(lista3))

print(lista4)
print("Salida 4: " + longestCommonPrefix(lista4))