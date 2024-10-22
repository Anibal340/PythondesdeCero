names=("Luis","diego","Andres","Carlos")
ages=[15,30,26,12,40]
text="Geekipedia"
print(names)
print(ages)
print(text)

print("\nFuncion zip() como iterable: \n")
combination=zip(names,ages,text)
print(combination)

print("\nFuncion zip() con la funcion list(): \n")
combination=list(zip(names,ages,text))
print(combination)

print("\nFuncion zip() con la funcion tuple(): \n")
combination=tuple(zip(names,ages,text))
print(combination)

print("funcion zip() con ciclo for")

for name, age,txt in zip(names,ages,text):
    print(name,age,txt)

