A={1,2,3,4,5}
print(f"Conjunto a: {A}")
B={1,2,3,4,5}
print(f"Conjunto b: {B}")
print("¿A es superconjunto de B?")
essuperconjunto = A.issuperset(B)
print("Utilizando el metodo issuperset():", essuperconjunto)

essuperconjunto = A>=B
print("Utilizando el operador >=:", essuperconjunto)

essuperconjunto = A>B
print("Utilizando el operador >:", essuperconjunto)