# Crear una funcion cuyos parametros sean una lista y un indice de posicion para mostrar el vlor de la lista en esa
# Ubicacion. 
    # que ocurre si ingreso un indice que se encuentra fuera del rango?
    # si el valor del indice ingresado se encuentra dentro del rango, mostrar el valor
    # en caso contrario, mostrar un mensaje de error


def mostrar_elemento(lista, indice):
    try:
        print("El elemento en la posicion", indice, "es:", lista[indice])
        return
    except IndexError:
        print("El indice ingresado se encuentra fuera del rango")
    except ValueError:
        print("El valor ingresado no es un entero")
    except:
        print("Ha ocurrido un error")

lista = [1, 2, 3, 4, 5]
mostrar_elemento(lista, 1)