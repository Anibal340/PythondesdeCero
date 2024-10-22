A={1,2,3,4,5}
B={4,5,6,7,8}

print(A)
print(B)

#Utilizando el metodo Difference()
esDiffSimConjuntoAB=A.symmetric_difference(B)
esDiffSimConjuntoBA=B.symmetric_difference(A)
#Utilizando el operador -
esDiffSimConjuntoOP= A^B
esDiffSimConjuntoOPB= B^A

print("La Diferencia de conjuntos utilizando el metodo symmetric_difference():",esDiffSimConjuntoAB)
print("La Diferencia de conjuntos utilizando el metodo symmetric_difference():",esDiffSimConjuntoBA)
print("La Diferencia de conjuntosA -conjuntoB utilizando el operador ^:",esDiffSimConjuntoOP)
print("La Diferencia de conjuntosB-conjuntoA utilizando el operador ^:",esDiffSimConjuntoOPB)