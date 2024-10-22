
filas =int(input("¿Cuantas filas tendra la matriz:?"))
columnas =int(input("¿Cuantas columnas tendra la matriz:?"))
matrix=[]

for f in range(filas):
    fila = []
    for c in range(columnas):
        fila.append(int(input(f"Introduce un elemento a la fila {f}: ")))
    matrix.append(fila)

for row in matrix:
    print(row)