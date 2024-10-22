print("Sistema para calcular el promedio de un alumno.")

nombre = input("Para comenzar, ¿Cual es tu nombre?: ")

matematicas = int(input(nombre + " Cual es tu calificacion en Matematicas: "))
quimica = int(input(nombre + " Cual es tu calificacion en Quimica: "))
biologia = int(input(nombre + " Cual es tu calificacion en Biologia: "))

promedio = (matematicas + quimica + biologia)/3
promedio = int(promedio)

if promedio >= 6:
    print("Felicidades " + nombre + " aprobaste, con promedio de: ",promedio)

print("Fin.")
