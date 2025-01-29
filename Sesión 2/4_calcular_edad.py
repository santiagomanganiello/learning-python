# Escribir un programa que le pida a un usuario su año de nacimiento y otro año,
# y que le diga qué edad tenía el usuario en el año ingresado

nacimiento = int(input("Ingrese su año de nacimiento: "))
actual = int(input("Ingrese el año actual: "))

edad = actual - nacimiento

if edad < 0:
    print("usted no ha nacido para esa fecha")
    exit()
elif edad == 0:
    print("usted nacio este año")
    exit()

print(f"Usted tiene {edad} años en el año {actual}")