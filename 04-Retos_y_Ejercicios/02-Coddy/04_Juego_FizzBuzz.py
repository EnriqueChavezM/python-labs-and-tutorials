"""
FizzBuzz es un juego de programación sencillo y clásico que se usa a menudo para enseñar lógica básica y flujo de control. El juego consiste en iterar a través de números desde 1 hasta un límite especificado. 
Para cada número:
    - Si el número es divisible por 3, el programa muestra "Fizz".
    - Si el número es divisible por 7, muestra "Buzz".
    - Si el número es divisible por 3 y por 7, muestra "FizzBuzz".
    - En caso contrario, simplemente muestra el número.
    - Recorre los números del 1 al número que ingresó el usuario y, en cada iteración, usa la función que creaste para calcular el resultado
    REGLA EXTRA:
    - Si el número contiene el dígito '3' pero no es divisible ni por 3 ni por 7, muestra "Almost Fizz".

"""
print("Welcome to FizzBuzz!")

#Funcion revicion de condiciones
def fizzbuzz(i):
    
    if i % 3 == 0 and i % 7 == 0:
        print("FizzBuzz")
            
    elif i % 3 == 0:
        print("Fizz")
        
    elif i % 7 == 0:
        print("Buzz")
        
    else:
        print(str(i))

#Funcion revisar regla extra
def Almostfizz (n):
    
    if "3" in str(n):
        
        if int(n) % 3 != 0 and int(n) % 7 != 0:
            print("Almost Fizz")
            
        else:
            fizzbuzz(int(n))
            
    else:
        fizzbuzz(int(n))

num =int(input("Ingrease un número:\n→ "))
for i in range(1, num + 1):
    Almostfizz(i)