"""
Primer ejemplo
    En una escuela de condicciones, se necesita un programa que dependiendo de la edad del usuario debe mostrar el tipo de licencia a la que tiene derecho.
   
     Condiciones:
    - Si el usuario tiene menos de 18 años, no tiene derecho a ninguna licencia.
    - Si el usuario tiene 18 años o más, pero menos de 21 años, tiene derecho a la licencia tipo A.
    - Si el usuario tiene 21 años o más, pero menos de 25 años, tiene derecho a la licencia tipo B.
    - Si el usuario tiene 25 años o más, tiene derecho a la licencia tipo C


#pedir al usuario que ingrese su edad
edad = int(input("¿Cuantos años tienes?: "))
if edad < 18:
    print("No tienes derecho a ninguna licencia.")
elif edad < 21:
    print("Tienes derecho a la licencia tipo A.")
elif edad < 25:
    print("Tienes derecho a la licencia tipo B.")
else:
    print("Tienes derecho a la licencia tipo C.")

"""

"""
Segundo ejemplo
    En una inductria se cuenta con un sistema de medicion de temperatura de agua, el cual dependiendo de la temperatura del agua debe mostrar un mensaje al usuario.

    Condiciones:
    - Si la temperatura del agua es menor a 0 grados, el agua esta "Freezing".
    - Si la temperatura del agua es mayor o igual a 0 grados y menor o igual a 15 grados, el agua esta "Cold".
    - Si la temperatura del agua es mayor a 15 grados y menor o igual a 25 grados, el agua esta "Mild".
    - En caso contrario, el agua esta "Hot".

#pedir al usuario que ingrese la temperatura del agua
temperatura = float(input("Ingrese la temperatura del agua en grados Celsius: "))
agua = "unset"

if temperatura < 0:
    agua = "Freezing"
elif temperatura <= 15:
    agua = "Cold"
elif temperatura <= 25:
    agua = "Mild"
else:
    agua = "Hot"    

print(f"El agua esta: {agua}.")

"""

"""
Tercer ejemplo
    Un código que recibe como entrada dos números n1 y n2 y un carácter operacional.
    Los valores posibles para caracteres operacionales son '+', '-', '/' y '*'. 
    
    Condiciones: 
    -Si op es '+', establece result con n1 + n2 
    -Si op es '-', establece result con n1 - n2
    -Si op es '/', establece result con n1 / n2
    -Si op es '*', establece result con n1 * n2.
"""
#pedir al usuario que ingrese dos numeros y un operador
n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))
op = input("Ingrese el operador (+, -, /, *): ")
result = 0

if op == "+":
    print(f"Result = {n1 + n2}")
elif op == "-":
    print(f"Result = {n1 - n2}")
elif op == "/":
    print(f"Result = {n1 / n2}")
elif op == "*":
    print(f"Result = {n1 * n2}")
else:
    print("Operacion no valida")