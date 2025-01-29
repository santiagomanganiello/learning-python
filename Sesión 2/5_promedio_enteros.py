# Crear un programa que le solicite al usuario 5 enteros y muestre por pantalla el promedio de ellos

num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese un número entero: "))
num3 = int(input("Ingrese un número entero: "))
num4 = int(input("Ingrese un número entero: "))
num5 = int(input("Ingrese un número entero: "))

promedio = int((num1 + num2 + num3 + num4 + num5) / 5)

print(f"El promedio de {num1}, {num2}, {num3}, {num4} y {num5} es: ", promedio)