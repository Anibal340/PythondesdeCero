print("Modificando vocales")
vocales = ["a","e","i","o","u"]
print(f"Lista Vocales: {vocales}")
vocales[1]="x"
print(f"Lista Vocales: {vocales}")


print("Modificando vocales[1]=2")
vocales = ["a","e","i","o","u"]
print(f"Lista Vocales: {vocales}")
vocales[1]="x"
print("Modificando vocales[-1]=x")
print(f"Lista Vocales: {vocales}")

print("Modificando vocales[2:4]=x,y")
vocales = ["a","e","i","o","u"]
print(f"Lista Vocales: {vocales}")
vocales[2:4]=["x","y"]
print(f"Lista Vocales: {vocales}")

print("Modificando vocales[1:3]=x,y")
vocales = ["a","e","i","o","u"]
print(f"Lista Vocales: {vocales}")
vocales[1:3]=["x","y"]
print(f"Lista Vocales: {vocales}")

print("Modificando vocales[1:3]=x,y,z")
vocales = ["a","e","i","o","u"]
print(f"Lista Vocales: {vocales}")
vocales[1:3]=["x","y","z"]
print(f"Lista Vocales: {vocales}")


print("Modificando vocales[:2]=x,y,z")
vocales = ["a","e","i","o","u"]
print(f"Lista Vocales: {vocales}")
vocales[:2]=["x","y","z"]
print(f"Lista Vocales: {vocales}")

print("Modificando vocales[0:3]=x,y")
vocales = ["a","e","i","o","u"]
print(f"Lista Vocales: {vocales}")
vocales[0:3]=["x","y"]
print(f"Lista Vocales: {vocales}")

print("Modificando vocales[0:3]=x,y")
vocales = ["a","e","i","o","u"]
print(f"Lista Vocales: {vocales}")
vocales[0:3]="x","y"
print(f"Lista Vocales: {vocales}")

print("Modificando vocales[:]=x")
vocales = ["a","e","i","o","u"]
print(f"Lista Vocales: {vocales}")
vocales[:]="x"
print(f"Lista Vocales: {vocales}")
