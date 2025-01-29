# Crear una función que simule un cumpleaños: dado un entero imprima "Que los cumplas feliz"
# esa cantidad de veces.

def feliz(cumpleaños):
    for i in range(cumpleaños):
        print("Que los cumplas feliz")
    
cumpleaños = int(input("Ingrese la cantidad de cumpleaños: "))
feliz(cumpleaños)