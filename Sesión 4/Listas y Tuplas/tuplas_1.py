
# Se quiere guardar información de los siguientes países: Francia, Argentina, Japón, Alemania, Perú.
# Crear una tupla para cada país que contenga su nombre, su capital y el continente donde se 
# encuentra.
# Guardar las tuplas en una lista.
# Hacer una función que reciba por parámetros la lista, e imprima la información de cada país 


Francia = ("Paris", "Francia", "Europa")
Argentina = ("Buenos Aires", "Argentina", "America")
Japon = ("Japon", "Tokyo", "Asia")
Alemania = ("Berlin", "Alemania", "Europa")
Peru = ("Lima", "Peru", "America")

lista = [Francia, Argentina, Japon, Alemania, Peru]

def imprimir_informacion(pais):
    print(f"Pais: {pais[0]}, Capital: {pais[1]}, Continente: {pais[2]}")

for pais in lista:
    imprimir_informacion(pais)