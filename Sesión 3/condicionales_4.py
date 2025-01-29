# Crear una función que dada una letra, imprima por pantalla la estación del año que representa.
# En caso de no representar ninguna estación mostrar un mensaje que diga “error”

choice = str(input("Ingrese V para verano, I para invierno, O para otono y P para primavera: "))

def season(choice):
    if choice == "v" or choice == "V":
        print("Verano")
    elif choice == "i" or choice == "I":
        print("Invierno")
    elif choice == "o" or choice == "O":
        print("Otono")
    elif choice == "p" or choice == "P":
        print("Primavera")
    else:
        print("Error")

season(choice)