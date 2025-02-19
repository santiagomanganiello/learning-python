# Division de dos números con manejo de errores

divisor = input("Ingrese el divisor: ")
dividendo = input("Ingrese el dividendo: ")

try:
    division = int(divisor) / int(dividendo)
    print(f"El resultado de la division es: {int(division)}")
except ZeroDivisionError:
    print("No se puede dividir por cero")
except ValueError:
    print("Los valores ingresados no son enteros")