"""*****************************************************************************************

Descripción general del proyecto

    - Construirás un programa sencillo para gestionar los gastos diarios.
    - ¡Ahora creemos el programa real!
        1. Crea un bucle while infinito.
        2. En cada iteración del bucle, obtén la entrada del usuario; esta será la elección (del 1 al 5 del menú)
        3. Maneja el primer caso: 
            3.1 Si la elección es igual a 5, sal del programa (bucle) y muestra: Exiting the Daily Expense Tracker. Goodbye!
            3.2 Maneja la opción donde el usuario añade un gasto (1)
                3.2.1. Inicializa al inicio del programa una lista de gastos vacía
                3.2.2. Cuando el usuario seleccione 1 como opción, obtén otra entrada del usuario, un float, y añade su valor a la lista de gastos.
                3.2.3. Después de añadir, muestra: Expense added successfully!
*****************************************************************************************"""

# Mensaje de bienvenida al programa
print("Welcome to the Daily Expense Tracker!\n")
# Mostrar Menú
print("""Menu:
1. Add a new expense
2. View all expenses
3. Calculate total and average expense
4. Clear all expenses
5. Exit""")

bucle = True
gastos = []
while(bucle):
    menu = int(input())#"Ingrese numero del  menu:\n→"
    if menu == 1:
        monto = float(input())#"Ingrese monto del gasto:\n→"
        gastos.append(monto)
        print("Expense added successfully!")
        
    elif menu == 5:
        bucle = False

print("Exiting the Daily Expense Tracker. Goodbye!")

#Extra
print(gastos)