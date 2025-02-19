# hacer una lista que guarde nombre apellido intento y nota de los alumnos
# Donde "intento" es la instanciia que está rindiendo. 1 si es la primera vez, 2 si es el primer recuperatorio
# y 3 si es el segundo recuperatiorio.

# Se pide hacer una funcion que, dado esta lista de diccionarios, devuelva el promedio de las notas en la primera oportunidad que 
# rindieron los alumnos.

# ¿ Como harian para generalizar la funcion y que el intento sea parametrizable? es decir, que no solamente
# sirve para el intento 1, si no que tambien pueda servir para los demás.

alumnos = [
    {
        "nombre": "Lautaro",
        "apellido": "Rodriguez",    
        "intento": 3,                                                   
        "nota": 10,
    },
    {
        "nombre": "Juan",
        "apellido": "Perez",    
        "intento": 2,                                                   
        "nota": 9,
    } ,
    {
        "nombre": "Maria",
        "apellido": "Gomez",    
        "intento": 2,                                                   
        "nota": 8,
    } ,
    {
        "nombre": "Pedro",
        "apellido": "Garcia",    
        "intento": 1,                                                   
        "nota": 7,
    } ,
    {
        "nombre": "Sofia",
        "apellido": "Lopez",    
        "intento": 1,                                                   
        "nota": 6,
    }
]

nombre_intento = {
    1: "primer intento",
    2: "recuperatorio",
    3: "segundo recuperatorio"
}

def promedio_notas(alumnos, intento):
    notas = []
    for alumno in alumnos:
        if alumno["intento"] == intento:
            notas.append(alumno["nota"])
    promedio = sum(notas) / len(notas)
    return promedio

parcial = int(input("Ingrese el intento: "))
print(f"El promedio de las notas del {nombre_intento[parcial]}({parcial}) es: {promedio_notas(alumnos, parcial)}")


