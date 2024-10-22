diccionario={"manzana": 2,
             "banana": 3,
             "naranja": 1
             }

print(f"{diccionario}")

# Intentamos agregar una clave que ya existe en el diccionario
retrun_value= diccionario.setdefault("banana",4)
print(F"El valor retornado de (banana,4) es: {retrun_value}")
print(F"el diccionario actualizado es: {diccionario}")

# Intentamos agregar una clave que no existe en el diccionario
retrun_value= diccionario.setdefault("kiwi")
print(F"El valor retornado de (kiwi) es: {retrun_value}")
print(F"el diccionario actualizado es: {diccionario}")

# Intentamos agregar una clave que no existe en el diccionario con valor de retorno
retrun_value= diccionario.setdefault("mango",5)
print(F"El valor retornado de (mango,5) es: {retrun_value}")
print(F"el diccionario actualizado es: {diccionario}")  