# Se requiere hacer un programa para enseñar a unos niños a contar.
# Crear una función que reciba un número entero e imprima por pantalla los números del 1 hasta ese número.
# con la estructura de control iterativa for.

def contar(num):
    for i in range(1, num + 1):
        print(i)

num = int(input("Ingrese un número: "))
contar(num)