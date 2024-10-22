
"""nums={0,1,2,3,4,5,6,7,8,9}

for n in nums:
    print(n*n)
"""
#Sin utilizar expresion de comprension
cuadrados=[]

for x in range(10):
    if x%2==0:
        cuadrado=x**2
        cuadrados.append(cuadrado)
    
print("Sin expresiones de compresion",cuadrados)

#Utilizando expresion de comprension
#[expresion for elemento in iterable if condicion]
cuadrados=[x**2 for x in range(10) if x%2==0]
print("Con expresiones de compresion",cuadrados )

print("Diccionario creado con expresiones de comprension:")

personas=[("Carlos",30),("Gerardo",25),("Maria",35)]

dict_personas={nombre:edad for nombre, edad in personas if edad>=30}

print("Diccionario personas:",dict_personas)

