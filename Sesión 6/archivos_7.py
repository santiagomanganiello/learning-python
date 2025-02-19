archivo_salas = open("Sesión 6/data/salas.txt", "r")
lineas = [linea.strip() for linea in archivo_salas.readlines()]
salas = set(lineas)

archivo_salas.close()


archivo_peliculas = open("Sesión 6/data/peliculas.txt", "r")

lineas = [linea.strip() for linea in archivo_peliculas.readlines()]
peliculas = set(lineas)

archivo_peliculas.close()

# El archivo debera tener el siguiente formato: {pelicula};{sala} y escribirlo en el csv

archivo_funciones = open("Sesión 6/data/funciones.csv", "w")

for pelicula, sala in zip(peliculas, salas):
    archivo_funciones.write(f"{sala};{pelicula}\n")
    print(f"{sala};{pelicula}")

archivo_funciones.close()