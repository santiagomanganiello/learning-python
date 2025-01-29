# Repetir el punto anterior pero con la expresión que determina que una letra NO es vocal.

letra = input("Ingrese una letra: ")

def es_vocal(letra):
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        return True
    else:
        return False

es_vocal(letra)

if es_vocal(letra) == True:
    print("Es vocal")
else:
    print("No es vocal")