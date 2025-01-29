# Repetir pero para la expresión que permite saber si un número es par y menor a 10.

num = int(input("Ingrese un número: "))

if num % 2 == 0 and num < 10:
    print("Es par y menor a 10")
elif num % 2 == 0 and num > 10:
    print("Es par y mayor a 10")
elif num % 2 != 0 and num > 10:
    print("No es par y mayor a 10")
elif num % 2 == 0 and num == 10:
    print("El número es 10")
else:
    print("No es par y menor a 10")