#Diccionario vacio
diccionario={}
print(f"Diccionario vacio: {diccionario}")
print()

#diccionario homogeneo
diccionario_age = {"Juan": 32, 
                   "Gerardo": 21,
                   "Luis": 25
                   }

print(f"Diccionario edades: {diccionario_age}")
print()

#Diccionario heterogeno

diccionario_dates={"name": "Brenda",
                   "last_name": "Flores",
                   "age": 22
                   }
print(f"Diccionario edades: {diccionario_dates}")
print()

#diccionario para almacenar listas y diccionario

dictionary_list={"a":{"a":1},
                 "b":[0,1,2]}

print(f"Diccionario con lista y diccionario: {dictionary_list}")
print()

#dictionario con clave numerica
dictionary_keys_num={4:1,
                     5:2,
                     6:3
                     }

print(f"Diccionario con clave numerica: {dictionary_keys_num}")
print()

#un diccionario no puede tener claves repetidas
diccionario_repeated_key={"Juan": 20,
                          "Gerardo": 30,
                          "Juan": 15
                          }

print(f"Diccionario con clave repetidas: {diccionario_repeated_key}")
print()

#un dictionario puede tener claves numericas o de tipo texto
dictionary={1:23,
            "juan": 5,
            -2: "hola"
            }
print(f"Diccionario con clave de distintos tipos de datos: {dictionary}")
print()