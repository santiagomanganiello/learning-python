# En un almacen están buscando la forma de hacer los cobros más automáticamente. para esto, se nos pide crear
# una función que reciba un número entero que representa lo que hay que cobrar, le pida al usuario
# ingresar un monto, y se vaya mostrando por pantalla cuánto falta para completar el pago.

def pagar(importe):
    total_pagado = 0
    while total_pagado < importe:
        print(f"El importe a pagar es de {importe - total_pagado} pesos. por favor, ingrese un monto")
        monto = int(input("Ingrese el monto: "))
        total_pagado += monto

    if total_pagado >= importe:
        print("¡Pago Realizado!")

importe = int(input("Ingrese el importe: "))
pagar(importe)