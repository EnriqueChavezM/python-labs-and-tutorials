import math

# 1. Obtener la raíz cuadrada de un número
raiz = math.sqrt(64)
print(raiz)  # Imprime: 8.0

# 2. Redondear números decimales
precio = 10.2
print(math.ceil(precio))   # Redondea hacia arriba -> Imprime: 11
print(math.floor(precio))  # Redondea hacia abajo  -> Imprime: 10

# 3. Calcular el área de un círculo (Fórmula: π * r²)
radio = 5
area = math.pi * math.pow(radio, 2)
print(f"El área del círculo es: {area:.2f}")  # Imprime: El área del círculo es: 78.54

# 4. Calcular el factorial de un número (5! = 5 * 4 * 3 * 2 * 1)
print(math.factorial(5))  # Imprime: 120