# Se quiere hacer un sistema en la facultad para que un alumno pueda ir guardando las materias
# que va haciendo. para eso, crear una funcion que le pregunte al usuario la materia que quiere almacenar,
# e ir guardando la informacion en una lista hasta que ingrese una 'X'.


materias = []
X = True

def guardar_materia(materia):
    materias.append(materia)
    return materias

while X == True:
    materia = input("Ingresa una materia: ")
    if materia == "X" or materia == "x":
        print("Las materias guardadas:")
        for materia in materias:
            print(materia)
        X = False
    else:
        guardar_materia(materia)