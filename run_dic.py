#Metodo numero 1
dict_name={
    "a": 1,
    "b": 2,
    "c": 3
}
print("Usando for simple")

for key in dict_name:
    print(f"{key}: {dict_name[key]}")

#metodo numero 2
print("usando Items")
dict_name={
    "a": 1,
    "b": 2,
    "c": 3
}
for key,value in dict_name.items():
    print(f"{key}: {value}")
