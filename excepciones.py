try:
    numero=int(input("Ingresa un numero: "))
    resultado=50// numero
    print(f"50/ {numero} =",resultado)

except Exception as e:
    print(f"El valor ingresado debe ser entero. Error! {e}")

except ValueError as ve:
    print(f"El valor ingresado debe ser entero. Error! {ve}")

except ZeroDivisionError as zde:
    print(f"No podes Dividir por cero: {zde}")

else:
    print("Operacion exitosa.")

finally:
    print("finally. - !Fin del programa¡")