
nums_tuple=(5,8,3,3,1,6,2)

print(f"Tupla Original: {nums_tuple}\n")

num=int(input("¿Cual de estos numeros quieres modificar por 0?:"))
nums_tuple=list(nums_tuple)

len_tuple=len(nums_tuple)

for index in range(len_tuple):
    if nums_tuple[index]==num:
        nums_tuple[index]=0

nums_tuple=tuple(nums_tuple)

print(f"Tupla Modificada: {nums_tuple} \n")