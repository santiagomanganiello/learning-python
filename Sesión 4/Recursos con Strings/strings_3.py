# Hacer una función que reciba dos strings, una string y una substring
# Es decir, que el primero contiene al segundo, se pide devolver el string habiendo 
# eliminado el substring mismo

# Ejemplo string: "Campeones del Mundo - 2022"
# Ejemplo substring: "2022"
# Resultado: "Campeones del Mundo - "

def eliminar_substring(string, substring):
    return print(string.replace(substring, ""))


eliminar_substring("Campeones del Mundo - 2022", "2022")




