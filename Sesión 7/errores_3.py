# Abrir archivos con manejo de errores

try: 
    archivo = open("Sesión 7/data/file.txt", "r")
    print("Se abrio el archivo correctamente")
    archivo.close()
except FileNotFoundError:
    print("No se pudo encontrar el archivo file.txt")