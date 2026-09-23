"""******************************************************************************************

Desafío 1:

Estás gestionando un libro de recetas digital donde cada receta se almacena como un diccionario. 
Cada diccionario contiene el nombre de la receta como clave y una lista de ingredientes como valor. 
Tu tarea es realizar varias operaciones para actualizar y gestionar el libro de recetas.

1. Crear el Libro de Recetas:
    1.1. Crea un diccionario llamado recipe_book con las siguientes recetas:
        - "Pancakes": ["flour", "milk", "eggs", "sugar"]
        - "Salad": ["lettuce", "tomato", "cucumber", "olive oil"]
2. Acceder a los Ingredientes:
    2.1. Imprime la lista de ingredientes para "Pancakes".
3. Añadir una Nueva Receta:
    3.1. Añade una nueva receta  al diccionario.
        -"Smoothie": ["banana", "milk", "honey"] 
4. Modificar una Receta:
    4.1. Añade "blueberries" a la receta "Smoothie".
5. Imprimir Todas las Recetas:
    5.1 Imprime el diccionario recipe_book completo para verificar las actualizaciones.
*******************************************************************************************"""
print("RECETARIO 📒")

x = True
recetario = {}

while x:
    add =  True
    conteo = 1
    print("""
Menu:
1. Agregar multiples Recetas
2. Revisar Recetas
3. Añadir 1 receta nueva
4. Agregar Ingrediente a Receta
5. Revisar recetario
6. Salir
""")
    menu = int(input("Ingrese numero de menu a ingresar\n→ "))

    if menu == 1: #Agregar multiples Recetas
        while add:
            clave = input(f"Ingrese receta No.{conteo}.\n→ ")
            valor = list(input(f"Ingrese Ingredientes de la receta {clave} separados por comas.\n→ ").split(","))

            recetario[clave] = valor
            continuar = input("Quiere agregar otra receta.\n¿ SI o NO?\n").upper() == "SI" 
            if continuar:
                conteo += 1
            else:
                add = False
                
    elif menu == 2: #Revisar Recetas
        receta = input("Ingrese receta a revisar\n→ ")
        if receta in recetario:
           print(recetario[receta])
        else:
            print("Receta no encontrada")

    elif menu == 3: #Añadir 1 receta nueva
        receta = input(f"Ingrese nueva receta.\n→ ")
        if receta in recetario:
            print(f"Receta {receta} ya existe")
        else:
            valor = list(input(f"Ingrese Ingredientes de la receta {clave} separados por comas.\n→ ").split(","))
            recetario[receta] = valor

    elif menu == 4: #Agregar Ingrediente a Receta
        receta = input(f"Ingrese receta a modificar.\n→ ")
        if receta not in recetario:
            print("Receta no encontrada")
        else:
            lista_ingredientes = recetario[receta]
            while add:
                ingrediente = input(f"Ingrese Nuevo Ingrediente de la Receta {clave}.\n→ ")
                lista_ingredientes.append(ingrediente)
                continuar = input("Quiere agregar otro ingrediente.\n¿ SI o NO?\n").upper() == "SI" 
                if not continuar:
                    add = False

    elif menu == 5: #Revisar recetario
        print(recetario)
    elif menu == 6: #Salir
        x = False
    else: 
        print("ERROR: Numero de menu invalido")