# Se tiene un archivo csv que contiene información sobre el stock de una librería. Se guarda por cada
# línea, el nombre del producto, el código, el precio por unidad y el stock actual, es decir:
# nombre;código;precio;stock

archivo = open("Sesión 6/data/stock.csv", "r")

b=[]

datos = archivo.readlines()

archivo.close()

for i in range(len(datos)):
    b.append(datos[i].split(";"))

for i in range(len(b)):
    print(f"Nombre de producto: {b[i][0]}")
    print(f"Codigo: {b[i][1]}")
    print(f"Precio: {b[i][2]}")
    print(f"Stock: {b[i][3]}")

# Hacer una funcion que reciba un diccionario que describa una linea del archivo y lo agruegue,
# Es decir que si recibe un diccionario con los datos de un producto, lo agregue a la lista.

# TO DO ⚠️