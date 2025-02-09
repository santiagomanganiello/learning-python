# Hacer una lista con 5 nombres, y realizar las siguientes actividades:
    # ✅ Cambiar el ultimo elemento de la lista y cambiar el último nombre por "Juan".
    # ✅ Olvidemonos que sabemos que tiene 5 elementos, ¿ Como podria saber cual es el ultimo 
    # Elemento si no se la longitud?
    
    # Devolver el nombre que este a dos posiciones del final. 
    # ¿ Como hacemos para que nos funcione para cualquier lista y no solo la que tenga 5 elementos?
    # Recorrer la lista e imprimir cada nombre por pantalla.
    # Imprimir por pantalla la lista con 3 repeticiones usar el operador de repeticion (*)


lista = ["Lautaro", "Lauta", "Lauta", "Lauta", "Lauta"]

lista[-1] = "Juan"

print(f"El ultimo elemento de la lista es: {lista[-1]}")


# Obtener el ultimo elemento de la lista sin saber si tiene elementos

print(f"El ultimo elemento de la lista es: {lista[len(lista) - 1]}")


# Devolver el nombre que este a dos posiciones del final. 

print(f"El nombre que esta a dos posiciones del final es: {lista[len(lista) - 2]}")


# Recorrer la lista e imprimir cada nombre por pantalla.

for i in range(len(lista)):
    print(f"El nombre en la posicion {i} es: {lista[i]}")


# Imprimir por pantalla la lista con 3 repeticiones usar el operador de repeticion (*)

print(f"La lista con 3 repeticiones es: {lista * 3}")

