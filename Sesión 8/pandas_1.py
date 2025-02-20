import pandas as pd

peliculas = {
    'nombre': [
        'Titanic', 'Kil Bill', 'Matrix', 'El padrino', 'Avatar',
        'Casablanca', 'El exorcista',  'Soy leyenda', 'El club de la pelea', 'Mujercitas'],
    'director': ['James Cameron', 'Quentin Tarantino', 'Hermanas Wachowski',
        'Francis Ford Coppola', 'James Cameron', 'Michael Curtiz',
        'William Friedkin', 'Francis Lawrence','David Fincher',
        'Greta Gerwig'],
    'año': [1997, 2003, 1999, 1972, 2009, 1942, 1973, 2007, 1999, 2019],
    'género': ['romance', 'acción', 'ciencia ficción', 'drama', 'ciencia ficción', 'drama', 'terror',
            'ciencia ficción', 'drama', 'drama'],
    'puntaje': [8.6, None, 6.9, 7.5, 9.1, 6.0, None, None, 9.4, 8.0]
    }

df = pd.DataFrame(peliculas)

# df.head(n) -> Muestra las primeras 5 filas en caso de no especificar 
# df.iloc[:3] -> Muestra las primeras 3 filas
# df.loc[:, ['año', 'puntaje']] -> Muestra las columnas anio y puntaje


# df.info() -> Información sobre el DataFrame - 1 ✅
# df.head(3) -> Mostrar las primeras 3 filas - 2 ✅
# print(df.loc[:, ['director', 'género']]) -> Muestra las columnas director y género - 3 ✅
# mostrar peliculas que sean de drama -> print(df[df['género'] == 'drama']) - 4 ✅
# que cantidad de peliculas hay en cada genero? -> print(df['género'].value_counts()) - 5 ✅
# mostrar las peliculas que tengan puntaje entre 6 y 8 y cuyo año de estreno sea anterior a los 200
# -> print(df[(df['puntaje'] > 6.0) & (df['puntaje'] < 8.0) & (df['año'] < 2000)]) - 6 ✅
# Mostrar las peliculas que tengan valor nulo -> print(df[df['puntaje'].isnull()]) - 7 ✅
# Calcular el promedio del puntaje de las peliculas -> print(df['puntaje'].mean()) - 8 ✅
# Ordenar las peliculas por nombre de forma descendente -> print(df.sort_values(by=['nombre'], ascending=False)) - 9 ✅
# mostrar las 3 peliculas mas antiguas -> print(df.sort_values(by=['año'], ascending=True).head(3)) - 10 ✅
# mostrar solo el nombre y el año de las 3 peliculas mas nuevas
# -> print(df.sort_values(by=['año'], ascending=False).head(3)[['nombre', 'año']]) - 11 ✅
# agregar una columna que indique si la pelicula fue vista o no, una pelicula fue vista cuando tiene un puntaje
# no nulo -> df['vista'] = df['puntaje'].notnull() -> print(df) -> 12 ✅