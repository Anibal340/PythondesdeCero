#Utilizando el metodo remove()
print("Utilizando el metodo remove()")
vocales={"a","e","i","o","u"}

vocales.remove("i")

print("vocales.remove(i)",vocales)

#Utilizando el metodo discard()
print("Utilizando el metodo discard()")
vocales={"a","e","i","o","u"}

vocales.discard("z")
print("vocales.discard(z)",vocales)

#Evitar el error utilizando el metodo remove()
print("Evitar el error utilizando el metodo remove()")
vocales={"a","e","i","o","u"}

elemento="z"
if elemento in vocales:
    vocales.remove(elemento)
    print("vocales.remove(elemento):",vocales)
else:
    print(f"{elemento} no esta en el conjunto vocales.")