dictionario={"a": 1,
             "b": 2,
             "c": 3
             }
print(dictionario)

print(f"\nlos valores del diccionario son:\n {dictionario.values()}")

print(f"Convirtiendo los values utilizando el contructor list()")
list_values=list(dictionario.values())

print(f"La lista es: {list_values}")
print(f"Posicion 1 de la lista Items:  {list_values[1]}")