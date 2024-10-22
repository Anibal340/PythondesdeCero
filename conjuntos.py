
print("Conjuntos creados con llaves {}:")
print("EJemplo #1: {5,1,3,2,4}")
conjunto={5,1,3,2,4}
print(conjunto)

print("EJemplo #2: {-1,0,5,-2,1,4}")
conjunto1={-1,0,5,-2,1,4}
print(conjunto1)

print("EJemplo #3: {e,o,a,u,i}")
conjunto2={"e","o","a","u","i"}
print(conjunto2)

print("EJemplo #4: {e,5,o,0,a,2,1}")
conjunto2={"e",5,"o",0,"a",2,-1}
print(conjunto2)

print("EJemplo #5: {5,1,1,1,3,5}")
conjunto2={5,1,1,1,3,5}
print(conjunto2)

print("EJemplo #6: {5,[3,2,4],1,0,6}")
conjunto2={5,(3,2,4),1,0,6}
print(conjunto2,"\n")

print("Ejemplo con la funcion set()\n")
print("EJemplo #7: [e,5,o,0,a,2,-1]")
lista =["e",5,"o",0,"a",2,-1]
conju=set(lista)
print(conju)

print("Ejemplo #8: String hola")
conj=set("hola")
print(conj)