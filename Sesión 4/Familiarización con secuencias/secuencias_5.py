# Se pide ahora crear 3 tuplas como las del ejercicio 5, con un nombre y una edad. A continuación, 
# guardarlas en una lista. Pensar, ¿De que nos servirá guardar las tuplas en una lista en vez de tenerlas 
# por separado? 


tupla1 = (input("Ingrese su nombre: "), int(input("Ingrese su edad: ")))

tupla2 = (input("Ingrese su nombre: "), int(input("Ingrese su edad: ")))

lista = [tupla1, tupla2]

print(f"La lista es: {lista}")

# Podria servir para recorrer la lista e imprimir cada tupla, asociar las tuplas con los nombres 
# y las edades.