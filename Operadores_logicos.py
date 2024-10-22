
print("Conjuncion (and)")

num_uno = int(input("Escribe un numero mayor a 2 y menor de 5:"))

if num_uno > 2 and num_uno <5:
    print("El numero",num_uno,"cumple con la condicion")

else:
    print("El numero",num_uno,"No cumple con la condicion")


print("Conjuncion (or)")

palabra= input("para cumplir la condicion escribe: si o yes ")
palabra = palabra.lower()

if palabra=="si" or palabra=="yes":
    print("La condicion se ha cumplido")
else:
    print("La condicion No se ha cumplido")


print("Conjuncion NOT")

num_1=int(input("Introduce un numero igual a 5: "))

if not num_1==5:
    print("El numero es diferente de 5 y si cumple la condicion")

else:
    print("El numero es igual a 5 y no cumple la condicion")
    
    
