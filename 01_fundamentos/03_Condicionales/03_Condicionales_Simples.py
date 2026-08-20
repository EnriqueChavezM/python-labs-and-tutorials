"""
Primer  ejemplo
    Crear un programa que pida al usuario el numero  de  años de su computadora y que le diga si es una computadora nueva, usada o vieja.

    Condiciones:
    - Si la computadora tiene menos o igual de 2 años, es nueva.
    - Si la computadora tiene más de 2 años, entonces es vieja.

#pedir al usuario que ingrese el numero de años de su computadora
anios = int(input("¿Cuantos años tiene su computadora?: "))

if anios >= 0 and anios <= 2:
    print("La computadora es nueva.")
else:
    print("La computadora es vieja.")

"""

"""
Segundo ejemplo
    Crear un programa que pida  la  edad del usuario y que le diga si es mayor de edad o menor de edad.

    Condiciones:
    - Si el usuario tiene menos de 18 años, es menor de edad.
    - Si el usuario tiene 18 años o más, es mayor de edad.
"""

#pedir al usuario que ingrese su edad
edad = int(input("¿Cuantos años tienes?: "))
if edad < 18:
    print("Eres menor de edad.")
else:
    print("Eres mayor de edad.")
print("Fin del programa.")


