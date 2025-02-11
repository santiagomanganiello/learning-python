carta_nueva = int(input("Ingrese la carta nueva: "))

cartas_en_mano = [1, 4, 6, 8]
orden_cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Insertar en la posición correcta sin usar sort()
pos = 0
while pos < len(cartas_en_mano) and cartas_en_mano[pos] < carta_nueva:
    pos += 1

cartas_en_mano.insert(pos, carta_nueva)

print("Cartas ordenadas:", cartas_en_mano)