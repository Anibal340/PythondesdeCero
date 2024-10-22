
names_tuple=("Ana","Gerardo","Maria","Carlos", "Valentina")

print(f"Tupla Original: {names_tuple}")

validor=0
while validor==0:
    num=int(input("Ingrese un numero entero entre 0 y 4:"))
    if num>=0 and num<=4:
        names_tuples=list(names_tuple)
        len_names=len(names_tuple)

        for index in range(len_names):
            if index==num:
                validor=1
                print(f"El nombre es: {names_tuples[index]}")
    else:
        print("¡Error¡: numero invalido vuelva a intentarlo.")
