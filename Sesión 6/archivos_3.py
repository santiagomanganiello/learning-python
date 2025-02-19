
archivo = open("data/compras.txt", "w")

producto = input("¿Qué agrego a la lista de compras? ")

while producto != "" and producto != "X" and producto != "x":
    archivo.write(producto + "\n")
    producto = input("¿Qué agrego a la lista de compras? ")

archivo.close()