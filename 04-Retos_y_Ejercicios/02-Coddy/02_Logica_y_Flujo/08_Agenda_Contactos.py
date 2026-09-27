"""******************************************************************************************

Desafío del Proyecto:

En este proyecto, construiremos paso a paso una aplicación de agenda de contactos, dividiéndola en funciones pequeñas y manejables.

1. Crea una función llamada 'display_menu' que muestre las opciones del menú principal de la agenda de contactos.
    1.1.  El menú debe incluir las siguientes opciones:
        - Agregar contacto
        - Ver contacto
        - Editar contacto
        - Eliminar contacto
        - Enumerar todos los contactos
        - Salir
2. Crea la función 'add_contact' que recibe un argumento
    2.1. 'contact_book' (un diccionario). 
    2.2. La función debe:
        2.2.1. Obtener la entrada para el nombre, teléfono, correo electrónico y dirección del contacto.
        2.2.2. Verificar si el nombre ya existe en el diccionario. Si es así, imprime: "Contact already exists!".
        2.2.3. Si no, guarda el contacto en el siguiente formato:
            contact_book[name] = {
                "phone": phone,
	            "email": email,
	            "address": address
                }
        2.2.4. Luego imprime: "Contact added successfully!".

*******************************************************************************************"""
# Función Menú
def display_menu():
    print ("""Contact Book Menu:
1. Add Contact
2. View Contact
3. Edit Contact
4. Delete Contact
5. List All Contacts
6. Exit
""")

#Función Guardar Contacto
def add_contact(contact_book):
    datos = {}
    nombre = input("Ingrese el nombre: ")
    tel = input(f"Ingrese el teléfono del contacto {nombre}: ")
    datos['phone'] = tel
    email = input(f"Ingrese el correo electrónico del contacto {nombre}: ")
    datos['email'] = email
    dire = input(f"Ingrese la dirección del contacto {nombre}: ")
    datos['address'] = dire

    # Verificar existencia de nombre
    if nombre in contact_book:
        print("Contact already exists!")
    else:
        contact_book[nombre] = datos
        print("Contact added successfully!")
        print(contact_book)

    

display_menu()

prueba = {
    "Bob": {
        "phone": "234-567-8901",
        "email": "bob@example.com", 
        "address": "456 Oak Ave"
        }
    }

add_contact(prueba)
