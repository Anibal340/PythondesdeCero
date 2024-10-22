dictionario={"a": 1,
             "b": 2,
             "c": 3
             }
print(dictionario)

print(f"\nlos elementos del diccionario son:\n {dictionario.items()}")

print(f"Convirtiendo Items a la lista utlizando el contructor list()")
list_items=list(dictionario.items())

print(f"La lista es: {list_items}")
print(f"Posicion 1 de la lista Items:  {list_items[1]}")