matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
print("Mostrar todos los elementos de la matriz fila por fila")

for row in matrix:
    print(row)

print("Mostrar todos los elementos de la matriz columna por columna")

for row in matrix:   
    for element in row:
        print(element)
        
print("Mostrar todos los elementos de la matriz en formato Matriz")

for row in matrix:  
    for element in row:
        print(element, end=" ")
    print()     