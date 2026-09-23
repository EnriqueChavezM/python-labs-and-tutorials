"""******************************************************************************************

Desafío 1:

Crea una función llamada create_student_dict que acepte tres parámetros: 
    1. name 
    2. age 
    3. major 

La función debe devolver un diccionario 
    - cuyas claves sean "name", "age" y "major"
    - cuyos valores sean los valores correspondientes pasados a la función.

Por ejemplo: 
llamar a create_student_dict("Alice", 20, "Computer Science") debe devolver un diccionario con los siguientes pares clave-valor:
    - Clave: "name", Valor: "Alice"
    - Clave: "age", Valor: 20
    - Clave: "major", Valor: "Computer Science"

*******************************************************************************************"""
"""def create_student_dict(name, age, major):
    # Escribe el código aquí
    diccionario = {
        "name" : name,
        "age"  : age,
        "major": major 
    }
    return diccionario

name = input("→")
age = int(input("→"))
major = input("→")

print(create_student_dict(name,age,major))"""

"""******************************************************************************************

Desafío 2:

Crea una función llamada create_book_dict que tome tres parámetros: 
    - title 
    - author
    - year. 

La función debe devolver un diccionario donde 
    - las claves son "title", "author" y "year"
    - los valores son los valores correspondientes pasados a la función.

*******************************************************************************************"""
"""def create_book_dict(title, author, year):
    # Escribe el código aquí
    diccionario = {
        "title" : title,
        "author": author,
        "year"  : year

    }
    return diccionario

title = input("Ingrese Titulo de libro:\n→ ")
author = input("Ingrese Nombre de Autoe:\n→ ")
year = input("Ingrese el año del libro:\n→ ")

print(create_book_dict(title,author,year))"""
"""******************************************************************************************

Desafío 3:

Acceder a los valores

Crea una función llamada get_capital que toma dos parámetros:
    1. country_capitals (un diccionario) 
    2. country_name (una cadena). 

La función debe devolver la ciudad capital del nombre del país dado utilizando el diccionario country_capitals.

*******************************************************************************************"""
"""def get_capital(country_capitals, country_name):
    # Escribe el código aquí
    return country_capitals[country_name]

add =  True
conteo = 1
diccionario = {}

while add:
    clave = input(f"Ingrese clave {conteo}.\n→ ")
    valor = input(f"Ingrese valor {conteo}.\n→ ")

    diccionario[clave] = valor
    print(diccionario)
    continuar = input("Quiere agregar un elemento mas.\n¿ SI o NO?\n").upper() == "SI" 
    if continuar:
        conteo += 1
    else:
        add = False

key = input("Ingrese clave a buscar\n→ ")
print(f"El valor de la Clave es: {get_capital(diccionario,key)}")"""

"""******************************************************************************************

Desafío 4:

1. Crea una función llamada update_employee_info que reciba tres parámetros:
    1.1. employee_dict (un diccionario) 
    1.2. key (una cadena de texto)  
    1.3. value. 
2. La función debe actualizar el employee_dict con la nueva key y value. 
3. Si la clave ya existe, su valor debe ser actualizado. 
4. Si la clave no existe, se debe añadir un nuevo par clave-valor. 
5. La función debe devolver el diccionario actualizado.

*******************************************************************************************"""
"""def update_employee_info(employee_dict, key, value):
    # Escribe el código aquí
    employee_dict[key] = value
    return employee_dict

add =  True
conteo = 1
diccionario = {}
print("Crear Diccionario\n")
while add:
    clave = input(f"Ingrese clave {conteo}.\n→ ")
    valor = input(f"Ingrese valor {conteo}.\n→ ")

    diccionario[clave] = valor
    print(diccionario)
    continuar = input("Quiere agregar un elemento mas.\n¿ SI o NO?\n").upper() == "SI" 
    if continuar:
        conteo += 1
    else:
        add = False
print(f"Diccionario creado\n{diccionario}")
key = input("Ingrese clave a añadir/modificar\n→ ")
value = input(f"Ingrese el valor para la  clave {key}\n→ ")
print(f"Diccionario final: {update_employee_info(diccionario,key,value)}")"""

"""******************************************************************************************

Desafío 5:

1. Crea una función llamada update_inventory que toma tres parámetros:
    1.1. inventory_dict (un diccionario)
    1.2. item (una cadena)
    1.3. quantity (un entero). 
2. La función debe actualizar el inventory_dict con el nuevo item y quantity. 
3. Si el ítem ya existe en el inventario, su cantidad debe incrementarse por la cantidad dada. 
4. Si el ítem no existe, se debe agregar un nuevo ítem con la cantidad dada. 
5. La función debe devolver el diccionario actualizado.

*******************************************************************************************"""
def update_inventory(inventory_dict, item, quantity):
    # Escribe el código aquí
    if item in inventory_dict:
        suma = int(inventory_dict[item]) + quantity
        """print(suma)
        print(type(suma))"""
        inventory_dict[item] = suma
    else:
        inventory_dict[item] = quantity

    return inventory_dict

add =  True
conteo = 1
diccionario = {}
print("Crear Diccionario\n")
while add:
    clave = input(f"Ingrese clave {conteo}.\n→ ")
    valor = input(f"Ingrese valor {conteo}.\n→ ")

    diccionario[clave] = valor
    print(diccionario)
    continuar = input("Quiere agregar un elemento mas.\n¿ SI o NO?\n").upper() == "SI" 
    if continuar:
        conteo += 1
    else:
        add = False
print(f"Diccionario creado\n{diccionario}")
key = input("Ingrese clave a añadir/modificar\n→ ")
value = int(input(f"Ingrese el valor para la  clave {key}\n→ "))
print(f"Diccionario final: {update_inventory(diccionario,key,value)}")