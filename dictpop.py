dict_name={"a": 1,
            "b": 2,
            "c": 3
            }

print(f"Diccionario Orginal: {dict_name}")

last_value=dict_name.pop("b")

print(f"Diccionario Modified: {dict_name}")
print(f"Valor eliminando: {last_value}")

print()
#cambiar la clave que no exista
dict_name={"a": 1,
            "b": 2,
            "c": 3
            }

print(f"Diccionario Orginal: {dict_name}")

last_value=dict_name.pop("z","No se encuentra la clave en el diccionario.")

print(f"Diccionario Modified: {dict_name}")
print(f"Valor eliminando: {last_value}")

