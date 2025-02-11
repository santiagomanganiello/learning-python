# Santiago armó una lista con el pedido de empanadas de su familia pero ahora quiere saber la cantidad 
# de gustos diferentes que tiene que pedir

docena_de_empanadas = ["carne", "pollo","verdura","carne","carne","pollo","carne","verdura","verdura","carne","pollo","pollo"]

carne = docena_de_empanadas.count("carne")
pollo = docena_de_empanadas.count("pollo")
verdura = docena_de_empanadas.count("verdura")

print(f"La cantidad de carne {carne}")
print(f"La cantidad de pollo {pollo}")
print(f"La cantidad de verdura {verdura}")