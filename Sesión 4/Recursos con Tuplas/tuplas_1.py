# Un matrimonio está organizando una fiesta y tiene que armar una lista de invitados. Cada uno tiene su propia 
# tupla y guarda en ella a todos los que quiere invitar.

# si alguien cancela tienen que sacarlo de la tupla. 
# Hacer una función que reciba la tupla y un nombre, y devuelva una nueva tupla sin el nombre pasado por 
# parámetro.

def quitar_invitado(tupla, nombre):
    return tuple([i for i in tupla if i != nombre])


esposo_invitados = ["Coscu", "Eze", "Seba", "Lauta", "Rodri"]
esposa_invitados = ["Flor", "Sabrina", "Karen", "Lorena"]

esposo_invitados = quitar_invitado(esposo_invitados, "Eze")
esposa_invitados = quitar_invitado(esposa_invitados, "Karen")

print(f"Invitados del esposo:{esposo_invitados}, Invitados de la esposa:{esposa_invitados}")

# Cuando ya tienen todos los invitados tienen que juntar sus tuplas, para eso se necesita una funcion
# que a partir de dos tuplas cree una sola que sea la combinacion de ambas tuplas

def juntar_tuplas(tupla1, tupla2):
    return tupla1 + tupla2


invitados = juntar_tuplas(esposo_invitados, esposa_invitados)


print(f"Todos los invitados:{invitados}")