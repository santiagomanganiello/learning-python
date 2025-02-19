# Se quiere hace un programa para pedirle a un usuario que ingrese un número entero, y en ese caso de que el
# valor ingresado no sea un número entero mostrarle un mensaje apropiado

# usar isnumeric()
# usar try-except

# Crear una funcion que solicite al usuario un numeor entero
# Usarla para calcular el producto entre dos numeros enteros ingresados

numero1 = input("Ingrese un numero: ")
numero2 = input("Ingrese el segundo numero: ")

if numero1.isnumeric() and numero2.isnumeric():
    try: 
        producto = int(numero1) * int(numero2)
        print(f"El producto de {numero1} y {numero2} es:", producto)
    except:
        print("Ha ocurrido un error")
else:
    print("Los valores ingresados no son enteros")