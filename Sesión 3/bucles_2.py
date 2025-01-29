# Se necesita una funcionalidad para ayudar a unos niños a aprender las tablas
# Crear una función que reciba un número entero e imprima por pantalla la tabla de ese número.

def multiplicar(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
print("Aplicacion para obtener la tabla del 10 de un número")
num = int(input("Ingesá el numero para multiplicar: "))
multiplicar(num)