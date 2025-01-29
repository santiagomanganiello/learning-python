numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese un segundo numero: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

operacion = int(input("Ingrese 1 para sumar, 2 para restar, 3 para multiplicar y 4 para dividir: "))

if operacion == 1:
    print("La suma es: ", suma)
elif operacion == 2:
    print("La resta es: ", resta)
elif operacion == 3:
    print("La multiplicacion es: ", multiplicacion)
elif operacion == 4:
    print("La division es: ", division)
else:
    print("Operacion no valida")

