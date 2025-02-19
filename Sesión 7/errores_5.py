# Se debe validar que se puedan jugar 2, 3 o 4 jugadores y no se pueden ingresar string, valor valido mostrarlo
def validar_jugadores(jugadores):
    try:
        jugadores = int(jugadores)
        if jugadores < 2:
            print("Debe haber al menos 2 jugadores")
            return
        elif jugadores >= 2 and jugadores <= 4:
            print(f"se va a jugar con {jugadores} jugadores")
        elif jugadores > 4:
            print("Se puede jugar con un máximo de 4 jugadores")
            return
    except ValueError:
        print("El valor ingresado no es un entero")
        return
    except:
        print("Ha ocurrido un error")
        return

jugadores = input("Ingrese la cantidad de jugadores:")

jugadores = validar_jugadores(jugadores)

