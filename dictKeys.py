dictionario={"a": 1,
             "b": 2,
             "c": 3
             }
print(dictionario)

print(f"\nlas claves del diccionario son:\n {dictionario.keys()}")

print(f"Convirtiendo las keys utilizando el contructor list()")
list_keys=list(dictionario.keys())

print(f"La lista es: {list_keys}")
print(f"Posicion 1 de la lista Items:  {list_keys[1]}")