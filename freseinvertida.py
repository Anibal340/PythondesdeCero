string=input("Introduce la frase a invertir:")
string_reversed=""


for character in string:
    string_reversed=character+string_reversed

print(f"String invertido: {string_reversed}")