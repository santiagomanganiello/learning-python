# Un chef está armando una lista de supermercado con los ingredientes a comprar.
# Solo quiere agregar un ingrediente a la lista si no lo escribio antes.
# Hacer un programa que inserte un nuevo elemento en la lista de strings.
# Solamente si el elemento que se desea insertar no se encuentra en la lista.

ingredientes = ['tomate', "queso", "cebolla", "huevo"]

def agregar_ingrediente(ingredientes, ingrediente):
    if ingrediente not in ingredientes:
        ingredientes.append(ingrediente)
        print(f"El ingrediente {ingrediente} ha sido agregado.")
        print(f"Los ingredientes actuales son: {ingredientes}")
    else: 
        print("El ingrediente ya existe")
    
    return ingredientes

nuevo_ingrediente = input("Ingrese el ingrediente que desea agregar: ").lower()
agregar_ingrediente(ingredientes, nuevo_ingrediente)
