
print("=========================================================================")
print("=Programa para determinar ¿Cual es el numero mas grande de tres numeros?=")
print("=========================================================================")
num1=int(input("ingrese el primer numero: "))
num2=int(input("ingrese el segundo numero: "))
num3=int(input("ingrese el tercero numero: "))

if num1>num2 and num1>num3:
    print("El numero ",num1,"es el mas grande de los tres.")

elif num2>num3:
    print("El numero ",num2,"es el mas grande de los tres.")

else:
    print("El numero ",num3,"es el mas grande de los tres.")
