
ticket_supermercado = [
    {
        "Producto": "Leche",
        "Precio unitario": 1200,
        "Cantidad": 2
    } ,
    {
        "Producto": "Pan",
        "Precio unitario": 400,
        "Cantidad": 10
    } ,
    {
        "Producto": "Arroz",
        "Precio unitario": 1500,
        "Cantidad": 2
    } ,
    {
        "Producto": "Cerveza",
        "Precio unitario": 1000,
        "Cantidad": 1
    } ,
    {
        "Producto": "Cafe",
        "Precio unitario": 500,
        "Cantidad": 2
    }
]

def monto_total(ticket_supermercado):
    monto_total = 0
    for producto in ticket_supermercado:
        monto_total += producto["Precio unitario"] * producto["Cantidad"]
    return monto_total

print(f"El total del ticket es: {monto_total(ticket_supermercado)}$")