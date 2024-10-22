diccionario={"manzana": 1.55,
             "banana": 3.55,
             "naranja": 1.25
             }

print(diccionario)
precio_manzana=diccionario.get("manzana")
print(f"El precio de la manazana es: {precio_manzana}")

precio_mango=diccionario.get("mango")
print(f"El precio de la manazana es: {precio_mango}")

precio_mango=diccionario.get("mango",4.55)
print(f"El precio de la manazana es: {precio_mango}")