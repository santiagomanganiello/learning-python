# Escribir la expresión para saber si un número es mas grande que otro.
# Guardarla en una variable de tipo bool e imprimirla por pantalla para ver su valor.

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

def es_mayor(num1, num2):
    if num1 > num2:
        return True
    else:
        return False

bool = es_mayor(num1, num2)

print(bool)