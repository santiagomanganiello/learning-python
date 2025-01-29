

fichas_necesarias = int(3)

def calcular_fichas(fichas_necesarias):
    total_fichas = 0

    while total_fichas < fichas_necesarias:
        print(f"Ingresá {fichas_necesarias - total_fichas} fichas (F) para comenzar")
        ficha_f = input("")
        if ficha_f == "F" or ficha_f == "f":
            total_fichas += 1
        else:
            print("Por favor solamente ingrese fichas reales (F)")

    if total_fichas >= fichas_necesarias:
        print("¡A jugar! 🚀")

calcular_fichas(fichas_necesarias)