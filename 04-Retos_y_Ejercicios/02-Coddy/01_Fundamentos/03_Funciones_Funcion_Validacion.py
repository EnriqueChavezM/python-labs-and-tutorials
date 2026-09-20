"""
Tema: Resumen - Función de validación
Ejercicio: 
    1. Escribe una función llamada `is_valid` que reciba dos argumentos de tipo cadena: nombre de usuario y contraseña.
    2. La función devolverá `True` si el nombre de usuario y la contraseña son válidos en el sistema; de lo contrario, devolverá `False`.
    3. Nuestro sistema solo contiene dos nombres de usuario válidos: "admin" y "user".
    4. La contraseña válida para el usuario "user" es "qweasd".
    5. Para el usuario "admin", ¡cualquier contraseña es válida!

"""
def is_valid(username, password):
    # Escribe el código aquí
    if username == "admin" or username == "user":
        if username == "user":
            if password == "qweasd":
                return True
            else:
                return False
        else:
            if password != "":
                return True
            else:
                return False
    else:
        return False

nombre = input("Ingrese nombre de usuario:\n→ ")
contraseña = input("Ingrese password:\n→ ")

print(is_valid(nombre, contraseña))