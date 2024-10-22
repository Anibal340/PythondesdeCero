string=input("Introduzca una string: ")

print(f"Todas las letras estan en minusculas?: {string.islower()}")
string=string.lower()
print(f"string en minuscula: {string}")

print(f"Todas las letras estan en mayusculas?: {string.isupper()}")
print(f"String en mayusculas: {string.upper()}")
print(f"string original: {string}")