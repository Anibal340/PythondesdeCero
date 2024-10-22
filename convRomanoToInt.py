try:
    valores_romanos ={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000

    }
    num_romano=input("Ingrese un numero Romano para convertir en entero: ")
    num_romano=num_romano.upper()
    num_entero=0
    valor_anterior=0
    for caracter in num_romano[::-1]:
        valor_actual=valores_romanos.get(caracter,0)

        if valor_actual<valor_anterior:
            num_entero-=valor_actual

        else:
            num_entero+=valor_actual

        valor_anterior =valor_actual
    print("Resultado ",num_entero)

except ValueError:
    print("El valor ingresado debe ser un numero Romano")
except Exception as e:
    print(f"Ingresar un numero romano valido: {e}")