"""******************************************************************************************

Desafío 1:

1.Crea una función llamada "print_employee_details" que tome un diccionario "employee_data" como argumento. 
    1.1. La función debe recorrer el diccionario e imprimir cada par clave-valor en el formato 'key: value'. 
    1.2. Si el diccionario está vacío, la función debe imprimir 'No data available'.

Por ejemplo
    -Tenemos un diccionario llamado employee_data:
        employee_data = {"name": "John", "age": 30, "department": "Sales"}
    -Salida de la función:
        - name: John
        - age: 30
        - department: Sales

*******************************************************************************************"""
print("\nDesafío 1:")
def print_employee_details(employee_data):
    # Escribe el código aquí
    if not employee_data:
        print("No data available")

    else:
        for key, valor in employee_data.items():
            print(f"{key}: {valor}")

diccionario1 = {
    "Alice": "HR", 
    "Bob": "Engineering", 
    "Diana": "Marketing"
    }
diccionario2 = {}
print_employee_details(diccionario1)
print_employee_details(diccionario2)

"""******************************************************************************************

Desafío 2:

1. Crea una función llamada 'print_product_details' que toma un diccionario 'product_data' como argumento. 
2. La función debe iterar a través del diccionario e imprimir cada par clave-valor en el formato 'Key: Value', con la primera letra de la clave en mayúscula.
3. Si el diccionario está vacío, la función debe imprimir 'No product information available'.
*******************************************************************************************"""
print("\nDesafío 2:")
def print_product_details(product_data):
    # Escribe código aquí
    if not product_data:
        print('No product information available')
    
    else:
        for key, valor in product_data.items():
            print(f"{key.title()}: {valor}")

diccionarioA = {
    "name":"Headphones",
    "brand":"Sony",
    "price":199.99,"stock":30
    }

diccionarioB = {}
print_product_details(diccionarioA)
print_product_details(diccionarioB)
