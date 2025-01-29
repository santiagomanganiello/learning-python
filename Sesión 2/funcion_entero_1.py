# Crear una función que reciba un número y muestre el anterior y el siguiente

def mostrar_numeros(num):
    print(f"El número anterior a {num} es: ", num - 1)
    print(f"El numero siguiente a {num} es: ", num + 1)

num = int(input("Ingrese un numero: "))

mostrar_numeros(num)