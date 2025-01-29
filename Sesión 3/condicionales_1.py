# Crear una función que dado un número, devuelva su valor absoluto. El valor absoluto de un número
# es el mismo número sin considerar el signo

num = int(input("Ingrese un número: "))

def valor_absoluto(num):
    if num < 0:
        return -num
    else:
        return num

print("El valor absoluto de", num, "es", valor_absoluto(num))