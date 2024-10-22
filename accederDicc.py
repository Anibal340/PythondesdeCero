
dictionario = {"a": 1,
             "e": 2
              }

print(dictionario)
print(f"clave a: {dictionario['a']}")
print(f"clave e: {dictionario['e']}")

print()

dictionario={"numbers": [18,20,28],
             "groups":{"a":1,"b":2}}

print(dictionario)

print(f"clave numbers: {dictionario['numbers']}")
print(f"clave groups: {dictionario['groups']}")

print(f"clave numbers: {dictionario['numbers'][1]}")
print(f"clave groups: {dictionario['groups']["b"]}")