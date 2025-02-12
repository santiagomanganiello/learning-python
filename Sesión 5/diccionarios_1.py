# En una escuela se quiere tener un sistema para guardar la información de sus estudiantes para tener
# mejor organizado sus datos.

# Crear un diccionario que sirve para representar a una persona en este contexto, pensar en las
# características que se consideren más relevantes para identificar a una persona (su nombre,
# DNI, edad, etc).

# Agregar al diccionario creado, un campo que sea otro diccionario y sirva para guardar el curso
# del estudiante y sus características (año, división, orientación, etc).

# Teniendo una lista de diccionarios de estudiantes, buscar en la lista la persona con mayor edad
# e imprimirla por pantalla.

estudiantes = [
    {
        "nombre": "Lauta",
        "apellido": "Rodri",
        "edad": 24,
        "dni": 123456789,
        "genero": "Femenino",
        "curso": "6°6°",
        "telefono": 123456789,
        "direccion": "Calle 123",
        "ciudad": "Buenos Aires",
        "pais": "Argentina",
    },
    {
        "nombre": "Juan",
        "apellido": "Perez",
        "edad": 22,
        "dni": 987654321,
        "genero": "Masculino",
        "curso": "5°4°",
        "telefono": 987654321,
        "direccion": "Avenida Siempre Viva",
        "ciudad": "Córdoba",
        "pais": "Argentina",
    },
    {
        "nombre": "Maria",
        "apellido": "Gomez",
        "edad": 21,
        "dni": 112233445,
        "genero": "Femenino",
        "curso": "4°3°",
        "telefono": 112233445,
        "direccion": "Calle Falsa 456",
        "ciudad": "Rosario",
        "pais": "Argentina",
    }
]


def buscar_estudiante_mayor_edad(estudiantes):
    estudiante_mayor_edad = None
    for estudiante in estudiantes:
        if estudiante_mayor_edad is None or estudiante["edad"] > estudiante_mayor_edad["edad"]:
            estudiante_mayor_edad = estudiante
    return estudiante_mayor_edad


estudiante_mayor_edad = buscar_estudiante_mayor_edad(estudiantes)
print(f"El estudiante de mayor edad es: {estudiante_mayor_edad['nombre']} {estudiante_mayor_edad['apellido']} del curso {estudiante_mayor_edad['curso']}")