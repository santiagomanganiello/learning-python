# Crear una tupla que guarde tu nombre y tu edad. Luego, imprimir
# por pantalla tu edad, accediendo al elemento de la tupla que corresponda.

tupla = (input("Ingrese su nombre: "), int(input("Ingrese su edad: ")))

print(f"Su edad es: {tupla[1]}")