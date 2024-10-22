A={1,2,3}
B={3,4,5}
print(A)
print(B,"\n")

#Utilizando el metodo union()

u_conjunto=A.union(B)

#Utilizando el operador |

u_conjunto_op=B|A

print("Union de conjuntos utilizando el metodo union():",u_conjunto)
print("Union de conjuntos utilizando el operador |:",u_conjunto_op)
