# En una fábrica, se hace un chequeo de calidad a los productos antes de cada entrega.
# El resultado del chequeo de la entrega se guarda en una lista de diccionarios, donde cada diccionario tiene
# Codigo del producto, Fecha de vencimiento y si paso el chequeo o no

# Se pide hacer una funcion que reciba esta lista de diccionarios y elimine todos los productos que no pasaron
# el chequeo. devolver en una tupla el diccionario con los elementos eliminados y la cantidad de elementos
# que quedaron en el diccionario


productos = [ {
    "producto_id": 1,
    "vencimiento": "2025-01-01",
    "checked": True
} ,
{
    "producto_id": 2,
    "vencimiento": "2025-02-05",
    "checked": False
} ,
{
    "producto_id": 3,
    "vencimiento": "2024-12-25",    
    "checked": True
} ,
{
    "producto_id": 4,
    "vencimiento": "2025-01-12",
    "checked": False
} ,
{
    "producto_id": 5,
    "vencimiento": "2025-07-14",
    "checked": True
}
]

def borrar_productos(productos):
    productos_borrados = tuple(producto for producto in productos if not producto["checked"])
    productos_filtrados = tuple(producto for producto in productos if producto["checked"])
    return productos_borrados, len(productos_filtrados)

productos_borrados, productos_filtrados = borrar_productos(productos)
print("Productos borrados:", productos_borrados)
print("Productos restantes:", productos_filtrados)