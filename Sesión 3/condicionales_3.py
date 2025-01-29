# Escribir código que dado dos enteros, determine si la suma de ambos da menos que 100.
# Si la suma de ambos es menor a 100, calcular cúanto falta para llegar a 100 y
# mostrar por pantalla un mensaje con ese valor. si la suma es mayor a 100, mostrar un mensaje diciendo
# Llega a 100.

# Extra: ¿Cómo harian para que el programa quede generalizado para cualquier limite, a eleccion del usuario
# y no solo para 100?


print("¡Juguemos! Ingresá dos números enteros.")
num1 = int(input("Ingresá el primer número: "))
num2 = int(input("Ingresá el segundo número: "))

limite = int(input("Ingresá el limite a la que quieres llegar: "))

if num1 + num2 < limite:
    print("La suma de", num1, "y", num2, "es menor a", limite, ". Faltan", limite - (num1 + num2), "para llegar a", limite)
else:
    print("La suma de", num1, "y", num2, "es mayor a", limite, ". Llega a", limite)