personas=(("Eduardo",26),("Maria",30),("Gerardo",20),("Valentina",22))
print(f"Tupla Original: {personas}")
personas=list(personas)
lng_list=len(personas)
for i in range(lng_list):
    for j in range(i+1,lng_list):
        if personas[i][1]>personas[j][1]:
            aux = personas[i]
            personas[i],personas[j]=personas[j],aux
print(f"La persona de menor edad es: {personas[0]}")
print(f"La persona de mayor edad es: {personas[-1]}")


