# Se tiene que hacer un ticket de supermercado que se pueda representar como una lista de tuplas
# (Producto, Precio).
# A) Hacer una funcion que reciba la lista, calcule y devuelva el total que hay que pagar.
# B) Ahora se tienen dos tickets. Juntar ambos y volver a calcular el total.



# A) Hacer una funcion que reciba la lista, calcule y devuelva el total que hay que pagar.


def calcular_total(ticket):
    total = 0
    for producto, precio in ticket:
        total += precio
    return total    

ticket1 = [("Leche", 50), ("Pan", 20), ("Jamon", 30)]
print(f"El total de la compra es de: {calcular_total(ticket1)}$")
