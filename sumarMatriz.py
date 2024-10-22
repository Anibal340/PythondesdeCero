matrixA= [[1,2,3],
          [4,5,6],
          [7,8,9]]


matrixB= [[1,2,3],
          [4,1,2],
          [1,1,0]]

matrixC = []



for ma in range(len(matrixA)):
    nueva_fila =[]
    for mb in range(len(matrixA[0])):
        nueva_fila.append(matrixA[ma][mb]+matrixB[ma][mb])
    matrixC.append(nueva_fila)


for row in range(len(matrixA)):
    if row !=1:
        print(f"{matrixA[row]}   {matrixB[row]}   {matrixC[row]}")
    else:
        print(f"{matrixA[row]} + {matrixB[row]} = {matrixC[row]}")

