# Se tiene un archivo con la pregunta "¿Como estas hoy?" llamado pregunta.txt se pide leerlo y mostrar
# la pregunta por pantalla para luego pedirle al usuario que ingrese una respuesta.
# despues de guardar la respuesta dada por el usuario en el archivo.

archivo = open("data/pregunta.txt", "r+")

lineas = archivo.readlines()
print(lineas)

respuesta = input("Respuesta: ")
archivo.write("\n" + respuesta)

archivo.close()