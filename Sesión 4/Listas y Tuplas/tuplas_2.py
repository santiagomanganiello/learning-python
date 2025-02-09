# Una libreria tiene un sistema que guarda los nombres de todos los libros que tienen
# en una lista de la siguiente forma: ["El principito", "It", "Sherlock Holmes" ...]
# Se quiere saber cuantos libros repetidos tienen.
# hacer codigo que imprima para cada titulo, cuantos ejemplares hay.

libros = ["El principito", "It", "Sherlock Holmes", "El principito", "It", "Sherlock Holmes", "El principito", "It", "Sherlock Holmes", "El principito", "It", "Sherlock Holmes"]

print(f"Principito: {libros.count('El principito')} ejemplares")
print(f"It: {libros.count('It')} ejemplares")
print(f"Sherlock Holmes: {libros.count('Sherlock Holmes')} ejemplares")