frase = input("Ingrese un texto: ")

letters=dict.fromkeys(frase,0)

for letter in frase:
    letters[letter]+=1

print(letters)