# Obtener una palabra, borrarle todas las 'a' e imprimirla por pantalla

palabra = input("Ingrese una palabra: ")
palabra_sin_a = palabra.replace("a", "")

print(f"La palabra {palabra} sin las 'a' es: {palabra_sin_a}")