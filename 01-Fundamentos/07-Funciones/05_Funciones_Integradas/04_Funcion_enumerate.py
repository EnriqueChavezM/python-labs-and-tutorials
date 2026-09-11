"""
Ejemplos prácticos
    1. En un bucle for convencional.
    Ideal para mostrar la posición de cada elemento:
"""
print("\nEJEMPLO 1\n")
tareas = ["Enviar correo", "Descargar reporte", "Limpiar datos"]

for indice, tarea in enumerate(tareas):
    print(f"Tarea #{indice}: {tarea}")

# Salida:
# Tarea #0: Enviar correo
# Tarea #1: Descargar reporte
# Tarea #2: Limpiar datos

"""
    2. Cambiando el índice de inicio (start)
    Si quieres que el conteo comience desde 1 en lugar de 0:
"""
print("\nEJEMPLO 2\n")
servidores = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

for num, ip in enumerate(servidores, start=1):
    print(f"Servidor {num}: {ip}")

# Salida:
# Servidor 1: 192.168.1.1
# Servidor 2: 192.168.1.2
# Servidor 3: 192.168.1.3

"""
    3. Convertir a una lista de tuplas
    Puedes usar list() para transformar el resultado de enumerate() directamente en una lista de pares (índice, valor):
"""
print("\nEJEMPLO 3\n")
frutas = ["Manzana", "Banana", "Uva"]
resultado = list(enumerate(frutas))

print(resultado)
# Salida: [(0, 'Manzana'), (1, 'Banana'), (2, 'Uva')]