
archivo = open("Sesión 6/data/colores.csv", "r")
lineas = [linea.strip() for linea in archivo.readlines()]
archivo_colores = open("Sesión 6/data/colores.txt", "w")

for linea in lineas:
    characters = linea.split(";")
    archivo_colores.write(f"A {characters[0]} {characters[2]} le gusta el color {characters[1]}\n")

print("Colores guardados")

archivo_colores.close()