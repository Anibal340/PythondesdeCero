print("Ejercicio 1: diccionario")
fruits={"manzanas": 5,
        "peras": 2,
        "naranjas": 4
        }
print(fruits)
##parte 1 

num_manzanas=fruits.get("manzanas")
print(f"Cantidad de manzanas con el metodo get(): {num_manzanas}")
num_manzanas=fruits["manzanas"]
print(f"Cantidad de manzanas consultando el valor: {num_manzanas}")
##parte 2

print("ejercicio 2")
fruits["banana"]=5
print(f"Valor asignado: {fruits}")
fruits.setdefault("mango", 6)
print(f"Metodo setDefault(): {fruits}")
fruits.update({"uva": 3})
print(f"Metodo Update(): {fruits}")

# parte 3

print("ejercicio 3")

del fruits["peras"]
print(f"Funcion del: {fruits}")

fruits={"manzanas": 5,
        "peras": 2,
        "naranjas": 4
        }
print(fruits)
fruits.pop("peras")
print(f"Metodo pop: {fruits}")
print()
print("Ejercicio 4 de diccionario ")

fruits={"manzanas": 5,
        "peras": 2,
        "naranjas": 4
        }
print(fruits)

keys_list=list(fruits.keys())
print(f"Lista claves: {keys_list}")
value_list=list(fruits.values())
print(f"Lista valor: {value_list}")
print()
print("Ejercicio # 5")
fruits={"uvas": 5,
        "peras": 2,
        "naranjas": 4
        }
print(fruits)
print("¿La clave manzana existe en el diccionario?:")

if "manzanas" in fruits:
    print(True)
else:
    print(False)

