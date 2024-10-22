A={1,2,3,4,5}
B={4,5,6,7,8}

print(A)
print(B)

#Utilizando el metodo Difference()
esDiffConjuntoAB=A.difference(B)
esDiffConjuntoBA=B.difference(A)
#Utilizando el operador -
esDiffConjuntoOP= A-B
esDiffConjuntoOPB= B-A

print("La Diferencia de conjuntos utilizando el metodo difference():",esDiffConjuntoAB)
print("La Diferencia de conjuntos utilizando el metodo difference():",esDiffConjuntoBA)
print("La Diferencia de conjuntosA -conjuntoB utilizando el operador -:",esDiffConjuntoOP)
print("La Diferencia de conjuntosB-conjuntoA utilizando el operador -:",esDiffConjuntoOPB)