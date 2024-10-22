print("====================================")
print("Sistema de control vacacional Rappi")
print("====================================")
print("La empresa posee 3 departamentos")
print("Atencion Al cliente")
print("Logistica")
print("Gerencia")
nombre = input("Nombre del empleado: ")
clave_dep= int(input("Ingrese Clave de Departamento: "))



if clave_dep==1:
    print("====================================")
    print("Atencion al Cliente")
    print("====================================")
    antiguedad = int(input("Ingrese La Antiguedad en anios del empleado:"))
    if antiguedad==1:
        print("El empleado",nombre," tiene 7 dias de vacaciones")
    elif antiguedad>=2 and antiguedad<=6:
        print("El empleado",nombre," tiene 14 dias de vacaciones")
    elif antiguedad>=7:
        print("El empleado",nombre," tiene 20 dias de vacaciones")
    else:
        print("Antiguedad no disponible")
        


elif clave_dep==2:
    print("====================================")
    print("Logistica")
    print("====================================")
    antiguedad = int(input("Ingrese La Antiguedad en anios del empleado:"))
    if antiguedad==1:
        print("El empleado",nombre," tiene 7 dias de vacaciones")
    elif antiguedad>=2 and antiguedad<=6:
        print("El empleado",nombre," tiene 15 dias de vacaciones")
    elif antiguedad>=7:
        print("El empleado",nombre," tiene 22 dias de vacaciones")
    else:
        print("Antiguedad no disponible")

elif clave_dep==3:
    print("====================================")
    print("Gerencia")
    print("====================================")
    antiguedad = int(input("Ingrese La Antiguedad en anios del empleado:"))
    if antiguedad==1:
        print("El empleado",nombre," tiene 10 dias de vacaciones")
    elif antiguedad>=2 and antiguedad<=6:
        print("El empleado",nombre," tiene 20 dias de vacaciones")
    elif antiguedad>=7:
        print("El empleado",nombre," tiene 30 dias de vacaciones")
    else:
        print("Antiguedad no disponible")

else:
    print("Clave de departamento no disponible")
    
print("Fin.")
