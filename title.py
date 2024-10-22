
firstname = input("Nombre: ")
lastname = input("Apellido: ")
fullname = f"{firstname} {lastname}"

print()
print(f"¿El formato del metodo title() se ha aplicado?: {fullname.istitle()}")
print(f"Aplicado el metodo title(): {fullname.title()}")
print(f"Volvemos a impimir el nombre: {fullname}")

print()
fullname=fullname.title()
print(f"¿El formato del metodo title() se ha aplicado?: {fullname.istitle()}")
print(f"Se ha aplicado el metodo title() de manera permanente: {fullname}")