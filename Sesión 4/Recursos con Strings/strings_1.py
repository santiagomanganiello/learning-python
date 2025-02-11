# Hacer una funcion que reciba una string y que imprima solamente los caracteres 
# que sean vocales.

def vocales(string):
    for i in string:
        if i in "aeiouAEIOU":
            print("vocal encontrada: ", i)

palabra = input("Ingrese una palabra: ")
vocales(palabra)