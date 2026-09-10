"""
Ejemplos prácticos
1. En cadenas de texto (str)
    Verifica si una palabra o caracter (subcadena) forma parte de un texto.
"""
print("1. En cadenas de texto (str)\n")
archivo = "reporte_mensual.csv"
print("archivo = ", archivo)
# Verificar extensión

print(f"'csv' in archivo: {'csv' in archivo}")        # True
print(f"'.pdf' in archivo: {'.pdf' in archivo}")       # False
print(f"'txt' not in archivo: {'txt' not in archivo}")    # True

"""
2. En listas y tuplas
Comprueba si un valor concreto está dentro de la lista de elementos.
"""
print("\n2. En listas y tuplas\n")
servidores_activos = ["192.168.1.1", "192.168.1.5", "192.168.1.10"]
print("servidores_activos = ", servidores_activos)
ip_buscar = "192.168.1.5"

if ip_buscar in servidores_activos:
    print(f"El servidor {ip_buscar} está en línea.")
else:
    print("Servidor no encontrado.")

"""
3. En diccionarios (dict)
Por defecto, el operador in busca únicamente en las claves (keys) del diccionario, no en los valores.
"""
print("\n3. En diccionarios (dict)\n")
usuario = {"nombre": "Ana", "rol": "Admin", "nivel": 5}
print("usuario = ", usuario)
# Busca en las claves:
print(f"'rol' in usuario: {'rol' in usuario}")         # True
print(f"'Admin' in usuario: {'Admin' in usuario}")       # False (porque Admin es un valor, no una clave)

# Para buscar en los valores:
print(f"'Admin' in usuario.values(): {'Admin' in usuario.values()}") # True

"""
4. Aplicación en bucles for
Además de evaluar condiciones, la palabra clave in se utiliza en la sintaxis de los bucles for para iterar a través de los elementos de una colección:
"""
print("\n4. Aplicación en bucles for\n")
frutas = ["Manzana", "Banana", "Uva"]
print("frutas = ", frutas)
# Aquí 'in' indica la secuencia que se va a recorrer
for fruta in frutas:
    print(f"Procesando: {fruta}")