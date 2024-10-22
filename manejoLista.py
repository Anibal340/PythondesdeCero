
long_lista = int(input("¿Cuantos numeros enteros contendra la Lista? "))

numeros =[]

for i in range(long_lista):
    numeros.append(int(input("Introduce un numero entero: ")))

print(f"\nLista: {numeros} \nLa suma total de los elementos es: {sum(numeros)}")