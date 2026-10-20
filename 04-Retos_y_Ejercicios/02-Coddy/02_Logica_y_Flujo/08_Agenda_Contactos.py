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
3. Crea una función llamada 'view_contact' que muestre los detalles de un contacto específico.
    3.1. Tu función debe:
        3.1.1. Aceptar un diccionario de agenda de contactos como parámetro
        3.1.2. Obtener un nombre de contacto de la entrada del usuario (usando input())
        3.1.3. Mostrar los detalles del contacto si se encuentra
        3.1.4. Imprimir "Contact not found!" si el contacto no existe
    3.2. Al mostrar un contacto, utiliza este formato exacto:
        3.2.1.  Name: [name]
                Phone: [phone]
                Email: [email]
                Address: [address]
4. Crea una función llamada 'edit_contact' que reciba un argumento: contact_book (un diccionario).
    4.1. Obtén la entrada para el nombre del contacto que el usuario desea editar.
    4.2. Verifica si el nombre existe en el contact_book:
        4.2.1. Si existe, solicita al usuario que ingrese nuevos valores para el teléfono, correo electrónico y dirección del contacto (¡en ese orden!).
        4.2.2. Si el usuario no proporciona ninguna entrada (presiona Enter), mantén el valor actual para ese campo (en este caso, la entrada será una cadena vacía, '').
        4.2.3. Actualiza la información del contacto en el diccionario.
        4.2.4. Imprime: "Contact updated successfully!".
    4.3. Si el contacto no existe, imprime: 
        4.3.1. "Contact not found!".
5. Crea una función llamada 'delete_contact' que reciba un argumento: contact_book (un diccionario).
    5.1. Obtén la entrada para el nombre del contacto que el usuario desea eliminar.
    5.2. Comprueba si el nombre existe en el contact_book:
        5.2.1. Si existe, elimina el contacto del diccionario.
        5.2.2. Imprime: "Contact deleted successfully!".
        5.2.3. Si el contacto no existe, imprime: "Contact not found!".
6. Crea una función llamada 'list_all_contacts' que reciba un argumento: contact_book (un diccionario).
    6.1. Verifica si el contact_book está vacío:
        6.1.1. Si está vacío, imprime: "No contacts available.".
        6.1.2. Si no está vacío:
            6.1.2.1. Recorre cada contacto en el diccionario e imprime su nombre, teléfono, correo electrónico y dirección en un formato legible.

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
    nombre = input("Ingrese Nombre de Contacto: ")

    # Verificar existencia de nombre
    if nombre in contact_book:
        print("Contact already exists!")
        return #salir si existe

    # Sin no existe  
    phone = input(f"Ingrese el teléfono del contacto {nombre}: ")
    email = input(f"Ingrese el correo electrónico del contacto {nombre}: ")
    address = input(f"Ingrese la dirección del contacto {nombre}: ")
    contact_book[nombre] = {"phone": phone, "email": email, "address": address}
    print("Contact added successfully!")

# Función Mostrar Contacto
def view_contact(contact_book):
    nombre = input("Ingrese Nombre de Contacto: ")
    if nombre in contact_book:
        print(f"Name: {nombre}")
        print(f"Phone: {contact_book[nombre]['phone']}")
        print(f"Email: {contact_book[nombre]['email']}")
        print(f"Address: {contact_book[nombre]['address']}")

    else:
        print("Contact not found!" )

# Función Editar Contacto
def edit_contact(contact_book):
    nombre = input("Ingrese Nombre de Contacto: ")
    if nombre in contact_book:
        phone = input(f"Ingrese el nuevo teléfono del contacto {nombre}: ")
        email = input(f"Ingrese el nuevo correo electrónico del contacto {nombre}: ")
        address = input(f"Ingrese la nueva dirección del contacto {nombre}: ")
        contact_book[nombre] = {"phone": phone, "email": email, "address": address}
        print("Contact updated successfully!")
    
    else:
        print("Contact not found!" )

# Función Eliminar Contacto
def delete_contact(contact_book):
    name = input("Ingrese Nombre de Contacto a Eliminar: ")
    if name in contact_book:
        contact_book.pop(name)
        print("Contact deleted successfully!")
        
    else:
        print("Contact not found!")
        
# Función Lista de Contactos
def list_all_contacts(contact_book):
    if contact_book:
        for key in contact_book:
            print(f"Name: {key}")
            print(f"Phone: {contact_book[key]['phone']}")
            print(f"Email: {contact_book[key]['email']}")
            print(f"Address: {contact_book[key]['address']}\n")
    else: 
        print("No contacts available.")

#display_menu()

prueba = {
    "Bob": {
        "phone": "234-567-8901",
        "email": "bob@example.com", 
        "address": "456 Oak Ave"
        },
    "Alice": {
        "phone": "123-456-7890", 
        "email": "alice@example.com", 
        "address": "123 Main St"
        }
    }
prueba2 = {}
#add_contact(prueba)
#view_contact(prueba)
#edit_contact(prueba)
#delete_contact(prueba)
list_all_contacts(prueba2)




