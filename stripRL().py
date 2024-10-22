#eejemplo 1 strip
cadena=" Hola Ernesto "
cadena=cadena.strip("s tHo")
print(cadena)

#ejemplo 2 rstrip

cadena1="\tHola Ernesto\n"
print(cadena1)
cadena1=cadena1.rstrip("s tHo\t\n")
print(cadena1)

#ejemplo 2 lstrip

cadena2="\tHola Ernesto\n"
print(cadena2)
cadena2=cadena2.lstrip("s tHo\t\n")
print(cadena2)