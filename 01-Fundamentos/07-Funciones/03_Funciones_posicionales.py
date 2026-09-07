"""
Primer ejemplo (*argg)
    sumar n numeros

def suma(*args):
    s = 0
    for i in args:
        s += i
    return s

resultado = suma(1,2,3,4,5,6)
print(resultado)
resultado = suma(1,2,3)
print(resultado)
resultado = suma(1,2,3,4,5,6,7,8,9,10)
print(resultado)
resultado = suma(1,6)
print(resultado)

"""

"""
Segundo ejemplo (**kwarg)
    pasar los datos de lenguajes deprogramacion de un usuario e imprimirlos

"""
def lenguaje(nombre, **kwargs):
    print(f'Hola {nombre}')
    print("Buscando información acerca de tus lenguajes favoritos")
    print("Cargando información \n")
    print("Información: ")
    contador = 0
    print(type(kwargs)) # Sirve para ver el tipo de dato
    for clave in kwargs:
        contador += 1 # Se le suma uno en cada vuelta
        print(f'Tu {contador} lenguaje favorito es: {kwargs[clave]}')

lenguaje("Antonio", lenguaje1 = "Ruby", lenguaje2= "Java", lenguaje3= "Python", lenguaje4 = "PHP")