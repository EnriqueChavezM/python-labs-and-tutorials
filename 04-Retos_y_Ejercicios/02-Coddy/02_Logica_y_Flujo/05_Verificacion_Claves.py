"""******************************************************************************************

Desafío 1:

- Estás gestionando un diccionario de datos de empleados, donde cada clave es el nombre de un empleado y el valor es su departamento. 
- Tu tarea es:
    - Comprobar si "Alice" es una clave en el diccionario.
    - Si existe, imprimir: "Alice is in the company."
    - Comprobar si "John" no es una clave en el diccionario.
    - Si no existe, imprimir: "John is not in the company."

*******************************************************************************************"""
print("\nDesafío 1:")
employees = {"Alice": "HR", "Bob": "Engineering", "Diana": "Marketing"}

# Escribe el código aquí
if "Alice" in employees:
    print("Alice is in the company.")
if "John" not in employees:
    print("John is not in the company.")

"""******************************************************************************************

Desafío 2:

1. Crea una función llamada "check_inventory" que acepte dos parámetros: 
    1.1. inventory (un diccionario cuyas claves son nombres de artículos y cuyos valores son cantidades)  
    1.2. item (una cadena que representa el artículo que se debe comprobar). 
2. La función debe:
    2.1. Comprobar si item existe como clave en el diccionario inventory.
        2.1.1. Si el artículo existe en el inventario (independientemente de la cantidad), devolver la cadena: "<item> is in stock. Quantity: <quantity>".
        2.2.2. Si el artículo no existe como clave en el inventario, devolver la cadena: "<item> is not in stock."
Nota: 
    Se considera que un artículo está «en stock» si existe en el diccionario del inventario, incluso si su cantidad es 0. La función solo debe comprobar la presencia de la clave, no el valor de la cantidad.

*******************************************************************************************"""
print("\nDesafío 2:")
def check_inventory(inventory, item):
    # Escribe código aquí
    if item in inventory:
        return f"{item} is in stock. Quantity: {inventory[item]}"
    else:
        return f"{item} is not in stock."

inventario = {
    "apple":10,
    "banana":5,
    "orange":7
    }

print(check_inventory(inventario,"banana"))
print(check_inventory(inventario,"strawberry"))