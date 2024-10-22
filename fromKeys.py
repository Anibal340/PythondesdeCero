sequence= ["uno","dos","tres"]

dictionario_fk=dict.fromkeys(sequence)
print(f"el diccionario sin valor es: {dictionario_fk}")

sequence= ["uno","dos","tres"]
value = 5
dictionario_fk=dict.fromkeys(sequence,value)
print(f"el diccionario secuencia y valor es: {dictionario_fk}")

sequence= {"uno": 1,"dos": 2,"tres": 3}
value = 5
dictionario_fk=dict.fromkeys(sequence,value)
print(f"el diccionario es: {dictionario_fk}")

#secuencias con textos
dictionario_fk={}.fromkeys("hola",1)
print(f"el diccionario es: {dictionario_fk}")

dictionario_fk={}.fromkeys("hola",[1,2,"hola"])
print(f"el diccionario es: {dictionario_fk}")

dictionario_fk={}.fromkeys("hola",{"juan":25,"Maria":22})
print(f"el diccionario es: {dictionario_fk}")