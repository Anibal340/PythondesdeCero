print("==========")
print("Conversor")
print("==========")

print("Menu de Opciones: ")
print("Presionar 1 para convertir de numero a palabra")
print("Presionar 2 para convertir de palabra a numero")
opcion = int(input("Cual es tu opcion deseada?: "))


if opcion==1:
    print("Conversor de numero a palabra")
    opcion_1 = int(input("Cual es tu numero que deseada convertir a palabra?: "))
    if opcion_1==1:
        print("El numero es UNO")
    elif opcion_1==2:
        print("El numero es DOS")
    elif opcion_1==3:
        print("El numero es TRES")
    elif opcion_1==4:
        print("El numero es CUATRO")
    elif opcion_1==5:
        print("El numero es CINCO")
    else:
        print("El numero seleccionado nos es valido")
elif opcion==2:
    print("Conversor de palabra a numero")
    opcion_2 = input("Cual es la palabra que deseada convertir a numero?: ")
    opcion_2 = opcion_2.lower()
    if opcion_2=="uno":
        print("El numero es 1")
    elif opcion_2=="dos":
        print("El numero es 2")
    elif opcion_2=="tres":
        print("El numero es 3")
    elif opcion_2=="cuatro":
        print("El numero es 4")
    elif opcion_2=="cinco":
        print("El numero es 5")
    else:
        print("El numero seleccionado no existe")
else:
    print("Opcion no disponible")

print("Fin.")
    
