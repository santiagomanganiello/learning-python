# Crear una función que reciba dos enteros y que retorne el resto y el cociente.

def mostrar_numeros(num1, num2):
    cociente = num1 // num2
    resto = num1 % num2
    print(f"El cociente de {num1} y {num2} es: ", cociente)
    print(f"El resto de {num1} y {num2} es: ", resto)

num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese un número entero: "))

mostrar_numeros(num1, num2)