nums={1,2,3,4,5}
print("recorriendo conjunto con el ciclo for")
for n in nums:
    print(n)

print("Recorriendo con el ciclo while")


conjunto_lista=list(nums)
indx=0
while indx<len(conjunto_lista):
    element=conjunto_lista[indx]
    print(element)
    indx +=1