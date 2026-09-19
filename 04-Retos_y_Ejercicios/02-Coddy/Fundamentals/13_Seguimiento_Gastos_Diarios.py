"""*****************************************************************************************

Descripción general del proyecto

    - Construirás un programa sencillo para gestionar los gastos diarios.
    - ¡Ahora creemos el programa real!
        1. Crea un bucle while infinito.
        2. En cada iteración del bucle, obtén la entrada del usuario; esta será la elección (del 1 al 5 del menú)
        3. Maneja el primer caso: 
            3.1. Si la elección es igual a 5, sal del programa (bucle) y muestra: Exiting the Daily Expense Tracker. Goodbye!
            3.2. Maneja la opción donde el usuario añade un gasto (1)
                3.2.1. Inicializa al inicio del programa una lista de gastos vacía
                3.2.2. Cuando el usuario seleccione 1 como opción, obtén otra entrada del usuario, un float, y añade su valor a la lista de gastos.
                3.2.3. Después de añadir, muestra: Expense added successfully!
            3.3. Maneja la opción para ver todos los gastos (2).
                3.3.1. Si la lista de gastos está vacía, muestra: No expenses recorded yet.
                3.3.2. De lo contrario, muestra la lista en el siguiente formato:
                    Your expenses:
                    1. 23.1
                    2. 35.5
                    3. 99.99
                    4. 15.2
            3.4. Gestiona la opción para calcular el gasto total y medio (3).
                3.4.1. Si la lista de gastos está vacía, muestra: No expenses recorded yet.
                3.4.2. De lo contrario, muestra la lista con el siguiente formato:
                    Total expense: 600.0
                    Average expense: 200.0
            3.5. Maneja la opción para borrar todos los gastos (4).
                3.5.1. Después de borrar la lista de gastos, muestra: All expenses cleared.
            3.6. Por último, maneja la opción en la que la elección del usuario no esté en el rango del 1 al 5. 
                3.6.1. Salida: Invalid choice. Please try again.

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

    elif menu == 2:
        if gastos == []:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for g in range(len(gastos)):
                print(f"{g+1}. {gastos[g]}")

    elif menu == 3:
        if gastos == []:
            print("No expenses recorded yet.")
        else:
            t_gasto = 0
            med_gasto = 0
            for i in gastos:
                t_gasto += i
            med_gasto = t_gasto / len(gastos)
            print(f"Total expense: {t_gasto}")
            print(f"Average expense: {med_gasto}")                                                  

    elif menu == 4:
        print("All expenses cleared.")
        gastos.clear()
        
    elif menu == 5:
        bucle = False

    else:
        print("Invalid choice. Please try again.")

print("Exiting the Daily Expense Tracker. Goodbye!")
