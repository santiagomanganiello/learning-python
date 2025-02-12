
peliculas = [

    {
        "nombre": "Avatar",
        "puntuacion": 6.8,
        "estreno": 2009,
    } ,
    {
        "nombre": "Star Wars",
        "puntuacion": 10,
        "estreno": 1977,
    } ,
    {
        "nombre": "Matrix",
        "puntuacion": 9.5,
        "estreno": 1999,
    } ,
    {
        "nombre": "El senor de los anillos",
        "puntuacion": 5,
        "estreno": 2001,
    } ,
    {
        "nombre": "Shrek",
        "puntuacion": 8.5,
        "estreno": 2001,
    } ,
    {
        "nombre": "Toy Story",
        "puntuacion": 9,
        "estreno": 1995,
    }
]

def mayor_puntuacion(peliculas):
    for pelicula in peliculas:
        if pelicula["puntuacion"] > 7:
            # print de la cantidad de estrellas segun la puntuacion de la pelicula
            estrellas_cantidad = pelicula["puntuacion"]
            estrella = "⭐" * int(estrellas_cantidad)
            print("Pelicula recomendada:", pelicula["nombre"], pelicula["puntuacion"], estrella)

mayor_puntuacion(peliculas)