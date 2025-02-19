def validar_jugadores(players):
    try:
        players = int(players)
        if players < 2:
            print("Debe haber al menos 2 jugadores")
            return
        elif players == 3 or players == 5:
            print("No se puede jugar con jugadores impares")
            return
        elif players >= 2 and players <= 6:
            print(f"se va a jugar con {players} jugadores")
        elif players > 6:
            print("Se puede jugar con un máximo de 6 jugadores")
            return
    except ValueError:
        print("El valor ingresado no es un entero")
        return
    except:
        print("Ha ocurrido un error")
        return

jugadores = input("Ingrese la cantidad de jugadores:")

jugadores = validar_jugadores(jugadores)