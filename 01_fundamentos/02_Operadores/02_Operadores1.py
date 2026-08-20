#Operadores aritmeticos
print("Operadores aritmeticos\n")
#Pedimos al usuario que ingrese dos numeros
numero1 = int(input("Ingrese el primer numero: "))  
numero2 = int(input("Ingrese el segundo numero: "))

#imprimimos los resultados de las operaciones aritmeticas
print("\nSuma: ", numero1 + numero2)
print("Resta: ", numero1 - numero2)
print("Multiplicacion: ", numero1 * numero2)
print("Division: ", numero1 / numero2)
print("Division entera: ", numero1 // numero2)
print("Modulo: ", numero1 % numero2)
print("Exponente: ", numero1 ** numero2)

#Operadores logicos
print("\nOperadores logicos\n")
#Valores booleanos
a = True
b = False
print("a = ", a)
print("b = ", b)
#imprimimos los resultados de las operaciones logicas
print("AND: ", a and b)
print("OR: ", a or b)
print("NOT a: ", not a)
print("NOT b: ", not b)

#Operadores relacionales
print("\nOperadores relacionales\n")
#Pedimos al usuario que ingrese dos numeros
numero3 = int(input("Ingrese el primer numero: "))
numero4 = int(input("Ingrese el segundo numero: "))

#imprimimos los resultados de las operaciones relacionales
print("\nIgual a: ", numero3 == numero4)
print("Diferente a: ", numero3 != numero4)
print("Mayor que: ", numero3 > numero4)
print("Menor que: ", numero3 < numero4)
print("Mayor o igual que: ", numero3 >= numero4)
print("Menor o igual que: ", numero3 <= numero4)

#Operadores de asignacion
print("\nOperadores de asignacion\n")
#Pedimos al usuario que ingrese un numero
numero5 = int(input("Ingrese un numero: "))
print("\nnumero = ", numero5)

#imprimimos los resultados de las operaciones de asignacion
numero5 += 10
print("\nnumero += 10 ")
print("numero = ", numero5)
numero5 -= 2
print("\nnumero -= 2")
print("numero = ", numero5)
numero5 *= 3
print("\nnumero *= 3")
print("numero = ", numero5)
numero5 /= 4
print("\nnumero /= 4")
print("numero = ", numero5)
numero5 //= 2
print("\nnumero //= 2")
print("numero = ", numero5)
numero5 %= 3
print("\nnumero %= 3")
print("numero = ", numero5)
numero5 **= 2
print("\nnumero **= 2")
print("numero = ", numero5)

