# Se pide hacer un programa que pida dos palabras: una que se quiera reemplazar y la palabra por la que
# se quiera reemplazar, cambie el texto y lo guarde en el archivo otra vez. Por ejemplo, si la función recibe
# “poco” y “mucho”, reemplaza “poco” por “mucho” todas las veces que aparezca en el texto.

archivo = open("Sesión 6/data/poema.txt", "r+")

lineas = [linea.strip() for linea in archivo.readlines()]

palabra = input("Ingrese la palabra a reemplazar: ")
nueva_palabra = input("Ingrese la nueva palabra: ")

def reemplazar_palabras(lineas, palabra, nueva_palabra):
    for i in range(len(lineas)):
        if palabra in lineas[i]:
            lineas[i] = lineas[i].replace(palabra, nueva_palabra)
    archivo.seek(0)
    for linea in lineas:
        archivo.write(linea + "\n")

reemplazar_palabras(lineas, palabra, nueva_palabra)

archivo.close()