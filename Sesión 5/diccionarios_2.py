# Enunvivero se guardan las plantas en una lista de diccionario con la siguiente información: especie, si
# necesita luz solar o no, y el precio.

# Ahora se necesita un sistema que guarde las plantas a medida que van llegando. Se pide
# hacer una función que reciba la lista de diccionarios de plantas, y los datos de la planta nueva y agregue
# esa planta a la lista de diccionarios.


plantas = [
    {"especie": "Rosa", "luz_solar": True, "precio": 15.0},
    {"especie": "Orquídea", "luz_solar": False, "precio": 25.5},
    {"especie": "Cactus", "luz_solar": True, "precio": 10.0},
    {"especie": "Helecho", "luz_solar": False, "precio": 12.0},
    {"especie": "Lavanda", "luz_solar": True, "precio": 18.0},
    {"especie": "Bambú de la suerte", "luz_solar": False, "precio": 22.0}
]


def nueva_planta(plantas, especie, luz_solar, precio):
    nueva_planta = {"especie": especie, "luz_solar": luz_solar, "precio": precio}
    plantas.append(nueva_planta)
    return plantas


print("Sistema de nuevas plantas agregadas")

especie = input("Ingrese la especie: ")
luz_solar = input("Luz solar (S/N)").strip().lower()
precio = float(input("Ingrese el precio: "))

luz_solar_value = True if luz_solar == "s" else False

nueva_planta(plantas, especie, luz_solar_value, precio)
print(plantas)
