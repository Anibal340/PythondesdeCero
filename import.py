#importar un modulo completo

import math

print("importar un modulo completo")
print(math.sqrt(25))
print(math.sin(30),"\n")

print("importar modulo con un alias")
import math as m
print(m.sqrt(25))
print(m.tan(30))

#importar solo lo necesario de un modulo
print("importar solo lo necesario de un modulo")

from math import sqrt,sin
print(sqrt(25))
print(sin(30))

#importar todo de un modulo (evitar en general)

print("importar todo de un modulo (evitar en general)")

from math import *
print(tan(30))
print(sin(30))
print(sqrt(25))