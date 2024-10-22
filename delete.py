print("============================================")
vocales = ["a","e","i","o","u"]
print(f"Lista inicial: {vocales}")
del vocales[3]
print(f"del vocales[3]: {vocales}")
print("============================================")

vocales = ["a","e","i","o","u"]
print(f"Lista inicial: {vocales}")
del vocales[0:2]
print(f"del vocales[0:2]: {vocales}")
print("============================================")

vocales = ["a","e","i","o","u"]
print(f"Lista inicial: {vocales}")
del vocales[:]
print(f"del vocales[:]: {vocales}")
print("============================================")

vocales = ["a","e","i","o","u"]
print(f"Lista inicial: {vocales}")
del vocales
print(f"del vocales: {vocales}")
print("============================================")