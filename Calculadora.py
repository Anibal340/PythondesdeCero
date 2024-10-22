##Calculadora
print("Calculadora con una sola variable")
print("==============================================")
print("=============Menu de opciones=================")
print("==============================================")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Division entera")
print("6. Exponente ")
print("7. Modulo o resto")
opcion=int(input("Elija la opcion, que desea realizar: "))

if opcion==1:
    print("suma")
    num1=int(input("Introduce el primer numero: "))
    num2=int(input("Introduce el segundo numero: "))
    res=num1+num2
    print("El resultado de la suma es: ",res)
elif opcion==2:
    print("Resta")
    num1=int(input("Introduce el primer numero: "))
    num2=int(input("Introduce el segundo numero: "))
    res=num12-num2
    print("El resultado de la resta es: ",res)
elif opcion==3:
    print("Multiplicacion")
    num1=int(input("Introduce el primer numero: "))
    num2=int(input("Introduce el segundo numero: "))
    res=num1*num2
    print("El resultado de la multiplicacion es: ",res)
elif opcion==4:
    print("Division")
    num1=int(input("Introduce el primer numero: "))
    num2=int(input("Introduce el segundo numero: "))
    res=num1/num2
    print("El resultado de la division es: ",res)
elif opcion==5:
    print("Division entera")
    print("Division")
    num1=int(input("Introduce el primer numero: "))
    num2=int(input("Introduce el segundo numero: "))
    res=num1/num2
    print("El resultado de la division entera es: ",round(res))
    
elif opcion==6:
    print("Exponente")
    num1=int(input("Introduce el primer numero: "))
    num2=int(input("Introduce el segundo numero: "))
    res=num1**num2
    print("El resultado de la division entera es: ",res)
elif opcion==7:
    print("Modulo o resto")
    num1=int(input("Introduce el primer numero: "))
    num2=int(input("Introduce el segundo numero: "))
    res=num1%num2
    print("El resultado de la division entera es: ",res)
else:
    print("Opcion no valida")
