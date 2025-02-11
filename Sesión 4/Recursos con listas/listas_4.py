# mostrar la lista de tareas pares que tocan y la lista impar


lista_enumerada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def recibir_enteros(lista):
    pares = []
    impares = []
    for i in range(len(lista)):
        if i % 2 == 0:
            impares.append(lista[i])
        else:
            pares.append(lista[i])
    return pares, impares

pares, impares = recibir_enteros(lista_enumerada)
print(f"Las tareas pares son: {pares}")
print(f"Las tareas impares son: {impares}")