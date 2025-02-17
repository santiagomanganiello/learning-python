# Una profesora tiene una lista de diccionarios para guardar las notas que sacaron sus alumnos
# en el ultimo parcial que tomó. Cada uno de esos diccionarios tiene el nombre del alumno, su apellido
# su ni y la nota que se saco.
    # Hacer una funcion que reciba este diccionario, y guarde las notas en un archivo csv, llamados notas.csv
    # Tiempo después de guardar las notas, la profesora quiso saber la cantidad de alumnos que aprobaron
    # Hacer una funcion que lea el archivo creado en el ejercicio anterior, y devolver la cantidad de alumnos aprobados
    # Mayor a 4 (cuatro)

notas_parcial = [

    {
        "nombre": "Pedro",
        "apellido": "Gomez",
        "dni": "12345678",
        "nota": 4.5
    } ,
    {
        "nombre": "Maria",
        "apellido": "Gomez",
        "dni": "12345678",
        "nota": 5
    } ,
    {
        "nombre": "Lauta",
        "apellido": "Rodriguez",
        "dni": "12345678",
        "nota": 2
    } ,
    {
        "nombre": "Juan",
        "apellido": "Perez",
        "dni": "12345678",
        "nota": 3
    } ,
    {
        "nombre": "Maria",
        "apellido": "Gomez",
        "dni": "12345678",
        "nota": 5
    } ,
    {
        "nombre": "Lauta",
        "apellido": "Rodriguez",
        "dni": "12345678",
        "nota": 2
    }
]

archivo = open("Sesión 6/data/notas.csv", "w")

def guardar_notas(parcial):
    for alumno in parcial:
        archivo.write(f"{alumno['nombre']};{alumno['apellido']};{alumno['dni']};{alumno['nota']}\n")
    return "Notas guardadas en el archivo notas.csv"

print(guardar_notas(notas_parcial))

archivo.close()

# Devolver alumnos aprobados

archivo = open("Sesión 6/data/notas.csv", "r")

def contar_aprobados():
    aprobados = 0
    for linea in archivo.readlines():
        nota = float(linea.split(";")[3])
        if nota >= 4:
            aprobados += 1
    return "La cantidad de alumnos aprobados es: " + str(aprobados)

print(contar_aprobados())