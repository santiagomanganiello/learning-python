# Crear una función que recuba un número entero e imprima los números primos entre 0 y el número ingresado.

num = int(input("Ingrese un numero: "));

for i in range(0, num + 1):
    if i % 2 == 0:
        print(i)