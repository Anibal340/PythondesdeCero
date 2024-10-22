
tuple=("001","Manzana","rojo"),("002","Pera","verde"),("003","Naranja","naranja")

print(tuple, "\n")

for code, fruit,color in tuple:
    print(f"la {fruit} tiene el codigo {code} y es de color {color}")