import random as r
print("Bienvenidos a (Adivina el numero Secreto)")
print("He seleccionado un numero entre 1 y 100 !Adivina cual es!")
n=r.randint(1,100)
indx=1
while indx<11:
    print(f"Intento {indx}/10 ")
    try:
        num=int(input("Ingresa tu Adivinanza: "))
        if num>n:
            print("El numero es mas pequeño")
        elif num<n:
            print("El numero es mas grande")
        
        else:
            print(f"¡Felicidades! ¡Has adivinado el numero secreto ({num}) en  {indx} intentos!")
            break
    except Exception as e:
        print(f"Debes ingresar un numero entero: {e}")
    except ValueError:
        print("Debes ingresar un numero entero.")
    

    indx=indx+1
if num!=n:
    print(f"Lo sentimos, El numero secreto era {n}. ¡Mejor Suerte la proxima!")

input("Presiona enter para Salir.")