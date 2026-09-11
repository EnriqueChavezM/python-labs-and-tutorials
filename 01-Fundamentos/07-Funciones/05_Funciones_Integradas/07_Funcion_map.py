"""****************************************************
                    Ejemplos prácticos

EJEMPLO 1. 
    Aplicando una función incorporada
    Imagina que tienes una lista de cadenas con números y quieres convertir todos esos elementos a enteros (int):

****************************************************"""

print("EJEMPLO 1. Aplicando una función incorporada\n")

textos_numeros = ["10", "20", "30", "40"]
print("Lista original de cadenas:", textos_numeros)
# Aplicamos la función int a cada elemento de la lista
resultado_map = map(int, textos_numeros)

# Convertimos el objeto map en una lista para ver el resultado
lista_numeros = list(resultado_map)

print("Lista de números convertidos:", lista_numeros)  # Muestra: [10, 20, 30, 40]

"""****************************************************

EJEMPLO 2.
   Supongamos que estás automatizando un sistema y necesitas calcular el IVA (16%) de una lista de precios: 

****************************************************"""

print("\nEJEMPLO 2. Usando una función personalizada\n")
# Definimos una función que calcula el precio con IVA
def calcular_iva(precio):

    return round(precio * 1.16, 2)

precios_netos = [100.0, 250.5, 50.0]

# Aplicamos nuestra función a toda la lista de precios
precios_con_iva = list(map(calcular_iva, precios_netos))
print("Lista de precios sin IVA:", precios_netos)
print("Lista de precios con IVA:", precios_con_iva)  # Muestra: [116.0, 290.58, 58.0]

"""****************************************************

EJEMPLO 3. Combinando map() con funciones lambda (Anónimas)
    Es muy común usar map() junto con funciones anónimas lambda para operaciones rápidas, como duplicar una lista de números:

****************************************************"""

print("\nEJEMPLO 3. Combinando map() con funciones lambda\n")
numeros = [1, 2, 3, 4, 5]

# Multiplica por 2 cada elemento usando una función lambda de una sola línea
duplicados = list(map(lambda x: x * 2, numeros))
print("Lista original de números:", numeros)
print("Lista de números duplicados:", duplicados)  # Muestra: [2, 4, 6, 8, 10]