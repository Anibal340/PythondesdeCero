

conjunto_a={1,2,3,4,5}
print(f"Conjunto a: {conjunto_a}")
conjunto_b={1,2,3,4,5}
print(f"Conjunto b: {conjunto_b}")
print("¿B es subconjunto de A?")
essubconjunto=conjunto_b.issubset(conjunto_a)
print("Utilizando el metodo issubset():", essubconjunto)

essubconjunto=conjunto_b<=conjunto_a
print("Utilizando el operador<=:", essubconjunto)

essubconjunto=conjunto_b<conjunto_a
print("Utilizando el operador<:", essubconjunto)