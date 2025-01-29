# Crear un programa que le solicite al usuario un entero y determine si es par 
# mostrando por pantalla un mensaje que indique el resultado.

num = int(input("Ingrese un número entero: "))

if num % 2 == 0:
    print("El número ingresado es par.")
else:
    print("El número ingresado es impar.")