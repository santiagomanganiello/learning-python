# Escribir código que recorra los números del 1 al 20 y que determine para cada uno si es par o impar, 
# imprimiendo un mensaje por pantalla en cada caso.

for i in range(1, 21):
    if i % 2 == 0:
        print(i, "es par")
    else:
        print(i, "es impar")