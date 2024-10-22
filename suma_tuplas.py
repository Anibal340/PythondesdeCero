tuple1=(1,2,3,4,5)
tuple2=(8,6,4,2,0)

print(f"Tupla 1: {tuple1}")
print("         +")
print(f"Tupla 2: {tuple2}")
suma=[]

for x,y in zip(tuple1,tuple2):
    suma.append(x+y)

print("         ===============")
suma=tuple(suma)
print(f"Suma:    {suma}")