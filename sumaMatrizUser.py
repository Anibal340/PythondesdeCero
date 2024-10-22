
cant_matriz=int(input("¿cuantas matrices vamos a sumar?: "))
if cant_matriz>1:
    filas =int(input("¿Cuantas filas tendra la matriz:? "))
    columnas =int(input("¿Cuantas columnas tendra la matriz:? "))

    matrix_list = []
    #llenado de matrices
    for number in range(cant_matriz):
        matrix=[]
        for row in range(filas):
            nueva_fila =[]
            for col in range(columnas):
                nueva_fila.append(
                    int(input(f"Introduce un elemento para la matriz {number+1} fila {row}, columna {col}: "))
                )
            matrix.append(nueva_fila)
        matrix_list.append(matrix)

    #suma de las matrices
    matrix=[]
    for row in range(filas):
        new_row=[]
        for colm in range(columnas):
            sum_matrix = 0
            for matriz_position in range(len(matrix_list)):
                sum_matrix+=matrix_list[matriz_position][row][colm]
            new_row.append(sum_matrix)
        matrix.append(new_row)
    matrix_list.append(matrix)

    #imprimir las matrices
    for matriz_row in range(filas):
        for matrix_list_position in range(len(matrix_list)):
            if matriz_row != 1:
                print(f"{matrix_list[matrix_list_position][matriz_row]}", end="   ")
            else:
                if matrix_list_position < len(matrix_list) - 2:
                    print(f"{matrix_list[matrix_list_position][matriz_row]}", end=" + ")
                elif matrix_list_position < len(matrix_list) - 1:
                    print(f"{matrix_list[matrix_list_position][matriz_row]}", end=" = ")
                else:
                    print(f"{matrix_list[matrix_list_position][matriz_row]}", end="   ")
        print()




else:
    print("se necesitan dos mas matrices para realizar la suma")