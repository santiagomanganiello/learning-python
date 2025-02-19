opciones = {
    1: "hamburguesas",
    2: "milanesas",
    3: "Goliat",
    4: "Alfajor Rasta",
    5: "Papas Fritas",
    6: "Agua",
}

valores = {
    1: 1000,
    2: 1500,
    3: 500,
    4: 300,
    5: 600,
    6: 350,
}

# se tiene estos dos diccionarios, se busca un programa que busque la informacion de la siguiente manera
    # hamburguesas -> 1000 ✅
# y pida al usuario una opción y una cantidad. luego , debe imprimir el total a pagar.
# se debe considerar que el usuario podria ingresar una opción que no está en el diccionario, o ingresar
# una opcion que no sea un número. se debe mostrar un mensaje de error en ese caso.

def mostrar_menu():
    print("--- MENU ---")
    for opcion in opciones and valores:
        print(opcion, ":", opciones[opcion], "->", valores[opcion])

def calcular_total(option, quantity):
        try:
            option = int(option)
            quantity = int(quantity)
            total = valores[option] * quantity
            return f"total a pagar: {quantity} {opciones[option]} -> ${total}"
        except KeyError:
            return "La opcion ingresada no se encuentra en el menu"
        except ValueError:
            return "El valor ingresado no es un entero"
        except:
            return "Ha ocurrido un error"

mostrar_menu()
opcion = input("Ingrese una opcion: ")
cantidad = input("Ingrese una cantidad: ")
print(calcular_total(opcion, cantidad))
