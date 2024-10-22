
frutas=["manzanas","platano", "uva","sandia"]
print(frutas)

print("\nRecorrido con for:")
for pos, fruta in enumerate(frutas, start=101):
    print(f"Posicion {pos}:{fruta}")

print("\nConvertido a lista:")
enumerado=list(enumerate(frutas,start=1))
print(enumerado)