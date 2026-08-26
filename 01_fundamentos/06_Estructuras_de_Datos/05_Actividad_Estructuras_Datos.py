"""
Caso
    Las agendas telefónicas son una guía donde se encuentran los datos de diferentes personas como su nombre, domicilio y teléfono. 
    Además, sirven para localizar personas, lugares o servicios. 

    Escribe un programa que permita guardar nombres y números de teléfono. 
    El programa nos dará el siguiente menú:
        (1) Consultar: pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono, si no indicar que no existe.
        (2) Añadir: pide un nombre. Si el nombre se encuentra en la agenda, indicar que ya existe, si no solicitar el número de teléfono.
        (3) Modificar: pide un nombre. Si el nombre no está en la agenda, indicar que no existe, sino solicitar el nuevo número de teléfono.
        (4) Borrar: pide un nombre. Si el nombre no está en la agenda, indicar que no existe, sino eliminar el número de teléfono.
        (5) Salir: si el usuario digita el número 5, detener el ciclo.

    Los datos para este ejercicio son los siguientes: 
        Jose : 302944
        Mario : 829455
        Angel : 829405
        Luis : 930594
"""
#funcion 
def mensaje_no():
    print("Este nombre no existe en la agenda")

# Definición de diccionario
agenda = {
    "Jose"  : 302944,
    "Mario" : 829455,
    "Angel" : 829405,
    "Luis"  : 930594,
}

#Variables
consulta =  True

#Ciclo
while consulta:
    #Mensaje de bienvenida
    print("\n MI AGENDA 📒")
    print("➿➿➿➿➿➿➿")
    print("1) Consultar \n2) Añadir \n3) Modificar \n4) Borrar \n5) Salir")

    #Variable local
    opcion = ""

    #Ciclo Anidado
    while opcion not in ("1", "2", "3", "4", "5"):
        opcion = input("→ ")

        #Condicionales
        if opcion == "1":
            #Pedir nombre
            #print(list(agenda.keys()))
            nombre = input("Ingrese nombre de consulta: \n → ")
            #Comprobar si nombre existe
            if nombre not in agenda:
                mensaje_no()
            else:
                telefono = agenda[nombre]
                print(nombre, ":", telefono)
        elif opcion == "2":
            #Pedir nombre
            nombre = input("Ingrese nombre para añadir: \n → ")
            if nombre in agenda:
                print("EL nombre ya existe en la agenda")
            else:
                #Pedir numero
                telefono = int(input("Digite el telefono: \n → "))
                #Añadir a la agenda
                agenda[nombre] = telefono
                print("El Telefono se ha añadido correctamente")
        elif opcion == "3":
            #Pedir nombre
            nombre = input("Ingrese nombre a modificar: \n → ")
            #Comprobar si nombre existe
            if nombre not in agenda:
                mensaje_no()
            else:
                #Pedir numero
                telefono = int(input("Digite el telefono: \n → "))
                #Añadir a la agenda
                agenda[nombre] = telefono
                print("El Telefono se ha modificado correctamente")
        elif opcion == "4":
            #Pedir nombre
            nombre = input("Ingrese nombre a borrar: \n → ")
            #Comprobar si nombre existe
            if nombre not in agenda:
                mensaje_no()
            else:
                #Borrar telefono
                del agenda[nombre]
                print("Se a borrado el contacto correctamente")
        elif opcion == "5":
            print("Gracias por utilizar el programa")
            consulta = False
        else:
            print("Opcion no valida")
    