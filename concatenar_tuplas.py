
print("****** Usando el operador +**************\n")
tupla1=(1,2,3)
tupla2=(4,5,6)
print(f"tupla1: {tupla1} | tupla: {tupla2}")
tupla_concatenada=tupla1+tupla2

print(f"la tupla concatenada es: {tupla_concatenada}\n")
#print(f"la tupla concatenada es: {tupla1}")

print("****** Usando el operador +=**************\n")
tupla1=(1,2,3)
tupla2=(4,5,6)
print(f"tupla1: {tupla1} | tupla2: {tupla2}")
tupla1+=tupla2
print(f"la tupla concatenada es: {tupla1}\n")

#Usando funcion tuple concatenacion con la lista 
print("****** Usando la funcion tuple()**************\n")
tupla11=(1,2,3)
lista=[4,5,6]
print(f"tupla1: {tupla1} | lista: {lista}")
tupla_concatenada=tupla11+tuple(lista)
print(tupla_concatenada,"\n")