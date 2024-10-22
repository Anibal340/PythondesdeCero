
tabla=int(input("¿Que tabla de multiplicar quieres ver?:"))
print(f"la tabla del {tabla} es: ")
for indice in range(0,11):
    print(f"{tabla}x{indice} = {tabla*indice}")