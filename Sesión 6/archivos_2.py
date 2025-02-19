# Si aparece santi en la lista, tambien agregar a tomi

archivo = open("Sesión 6/data/regalo.txt", "r+")

lineas = [linea.strip() for linea in archivo.readlines()]
nombres_recaudados = set(lineas)

if "Santi" in nombres_recaudados:
    nombres_recaudados.add("Tomi")

def contar(nombres):
    return len(nombres) * 1000

total = contar(nombres_recaudados)

print(f"El total recaudado es: {total}$")

archivo.seek(0)
archivo.truncate()
archivo.write("\n".join(nombres_recaudados))
archivo.close()