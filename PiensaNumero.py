import random as r
print("Piensa en un numero de 1 a 100. yo tratare de adivinarlo.")

intentos=0
adivinanza_minima=1
adivinanza_maxima=100
adivinanza_actual=0

while True:
    intentos+=1
    adivinanza_actual=r.randint(adivinanza_minima,adivinanza_maxima)

    print(f"¿Es {adivinanza_actual} tu numero?")
    respuesta=input("Ingresa mayor, menor, o correcto: ").lower()

    if respuesta == "correcto":
        print(f"¡Adivine tu numero ({adivinanza_actual}) en {intentos} intentos!")
        break
    elif respuesta == "mayor":
        adivinanza_minima=adivinanza_actual+1
    elif respuesta == "menor":
        adivinanza_maxima=adivinanza_actual-1
    else:
        print("Respuesta no valida. Ingresa mayor, menor o correcto.")