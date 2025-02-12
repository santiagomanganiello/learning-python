# Se quiere guardar la información de un grupo de maratonistas. Se necesita guardar su nombre, DNI
# y todas las maratones que corrió, de la cual a su vez se quiere tener el nombre de cada una, el año,
# el puesto en que salió el maratonista, y el tiempo que tardo en terminarla

# Crear el diccionario
# Ordenarlos alfabeticamente
# Ordenar las maratones de cada maratonista segun el tiempo que tardó en completar cada una de forma ascendente


maratonistas = [
    {
        "nombre": "Carlos López",
        "DNI": "12345678",
        "maratones": [
            {"nombre": "Maratón de Boston", "año": 2022, "puesto": 5, "tiempo": "2h 45m"},
            {"nombre": "Maratón de Nueva York", "año": 2023, "puesto": 12, "tiempo": "2h 50m"},
        ]
    },
    {
        "nombre": "María González",
        "DNI": "87654321",
        "maratones": [
            {"nombre": "Maratón de Chicago", "año": 2021, "puesto": 3, "tiempo": "2h 38m"},
            {"nombre": "Maratón de Berlín", "año": 2022, "puesto": 7, "tiempo": "2h 42m"},
            {"nombre": "Maratón de Londres", "año": 2023, "puesto": 5, "tiempo": "2h 40m"},
        ]
    },
    {
        "nombre": "Javier Rodríguez",
        "DNI": "11223344",
        "maratones": [
            {"nombre": "Maratón de Tokio", "año": 2020, "puesto": 15, "tiempo": "2h 55m"},
            {"nombre": "Maratón de París", "año": 2022, "puesto": 10, "tiempo": "2h 47m"},
        ]
    },
    {
        "nombre": "Lucía Fernández",
        "DNI": "55667788",
        "maratones": [
            {"nombre": "Maratón de Madrid", "año": 2019, "puesto": 2, "tiempo": "2h 35m"},
            {"nombre": "Maratón de Barcelona", "año": 2021, "puesto": 4, "tiempo": "2h 39m"},
        ]
    }
]

# Ordenarlos alfabeticamente
sorted(maratonistas, key=lambda x: x["nombre"])

# Ordenar las maratones de cada maratonista segun el tiempo que tardó en completar cada una de forma ascendente
for maratonista in maratonistas:
    maratonista["maratones"].sort(key=lambda x: x["tiempo"])

for maratonista in maratonistas:
    print("Nombre:", maratonista["nombre"])
    print("DNI:", maratonista["DNI"])
    print("Maratones:")
    for maraton in maratonista["maratones"]:
        print("Nombre:", maraton["nombre"])
        print("Año:", maraton["año"])
        print("Puesto:", maraton["puesto"])
        print("Tiempo:", maraton["tiempo"])
        print()