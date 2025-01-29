# Crear el programa al que sea imposible ganarle en el juego de "Piedra, papel o tijera".
# Cada elemento va a ser representado con una letra: R (piedra), P (papel) y T (tijera).

# Hacer una función que le haga al usuario ingresar alguna de esas letras, e imprimirla por pantalla.

def pedir_letra(letra):
    while letra != "R" and letra != "P" and letra != "T":
        print("NO vale")
        letra = input("Ingrese una letra: ")
    return letra

print("¡Juguemos! Ingresá piedra (R), papel (P) o tijera (T).")
letra = input("Tu letra: ")
letra = pedir_letra(letra)

if letra == "R":
    print("Papel. ¡Te gané! 😝")
elif letra == "P":
    print("Tijera. ¡Te gané! 😝")
elif letra == "T":
    print("Piedra. ¡Te gané! 😝")
else:
    print("No ingresaste una letra.")