# Dada una secuencia de palabras, invertir el orden de las palabras e imprimir la oración resultante

lista = ["entender", "pueden", "humanos", "los", "que", "código", "escriben", "programadores", "buenos", "Los", "entiende.", "computadora", "una", "que", "código", "escribe", "tonto", "cualquier"]

lista.reverse()

def oracion(lista): 
    oracion = ""
    for i in range(len(lista)):
        oracion = oracion + " " + lista[i]
    return oracion

print(oracion(lista))