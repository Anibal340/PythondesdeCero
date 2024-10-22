import random
# randint(), deveuelve un entero aleatoria en el rango [a,b]

num =random.randint(1,100)

print("num =random.randint(1,100):",num)

#Random, devuelve un numero de punto flotante en el rango [0.0,1.0]

num = random.random()

print("num = random.random():",num)

#Randrenge(), devuelve un elemento aleatorio de la secuencia generada por range(start,stop,step)
num=random.randrange(0,100,2)

print("num=random.randrange(0,100,2):",num)