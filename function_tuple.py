#Ejemplo 1 Crear una coordenada con tuple()

print("********** Ejemplo #1 *************")
x= 10
y=5
print(f"Las coordenadas son: {x},{y}")
coordenada=tuple([x,y])
print(f"La tupla es: {coordenada}")

#Ejemplo 2 Convertir un string a tupla

print("********** Ejemplo #2 *************")

string=input("Introduce una frase: ")

string_tuple=tuple(string)
print(f"La tupla es: {string_tuple}")

print("********** Ejemplo #3 *************")
numbers_dict={
  "uno": 1,
  "dos": 2,
  "tres": 3
 }
print(numbers_dict,"\n")
numbers_tuple=tuple(numbers_dict)
print(f"La tupla es: {numbers_tuple}")

#Convertir diccionario a tupla (valores)
print("********** Ejemplo #4 *************")
numbers_dict={
  "uno": 1,
  "dos": 2,
  "tres": 3
 }
print(numbers_dict,"\n")
numbers_tuple=tuple(numbers_dict.values())
print(f"La tupla es: {numbers_tuple}")

#Ejemplo 5 Convertir un diccionario a tupla (items)
print("********** Ejemplo #5 *************")
numbers_dict={
  "uno": 1,
  "dos": 2,
  "tres": 3
 }
print(numbers_dict,"\n")
numbers_tuple=tuple(numbers_dict.items())
print(f"La tupla es: {numbers_tuple}")
