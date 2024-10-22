##condicional compuesta
"""
num_uno=5
if num_uno==5:
    print("El numero es cinco")

else:
    print("El numero No es cinco")
"""
print("Sistema para calcular el promedio de un alumno.")

nombre = input("Para comenzar, ¿Cual es tu nombre?: ")

matematicas = int(input(nombre + " Cual es tu calificacion en Matematicas: "))
quimica = int(input(nombre + " Cual es tu calificacion en Quimica: "))
biologia = int(input(nombre + " Cual es tu calificacion en Biologia: "))

promedio = (matematicas + quimica + biologia)/3


if promedio >= 6:
    print("Felicidades " + nombre + " aprobaste, con promedio de: ",promedio)
    print("Felicidades " + nombre + " aprobaste, con promedio de: ",round(promedio,1))
else:
    print("Lo sentimos "+nombre+" Reprobado, con un promedio de: ",promedio)
    print("Lo sentimos "+nombre+" Reprobado, con un promedio de: ",round(promedio,1))
print("Fin.")
