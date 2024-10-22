lista = ["A","b","B","c","E","E","f"]

print(f"Lista Original: {lista}")

elemento=input("Introduce el elemento que deseas eliminar: ")
for caracter in lista:
    if elemento.lower() in lista:
        lista.remove(elemento.lower())
    elif elemento.upper() in lista:
        lista.remove(elemento.upper())

print(f"Elemento eliminado: {lista}")




