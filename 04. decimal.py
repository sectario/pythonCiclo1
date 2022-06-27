import math


number = float(input("Ingrese un numero con decimales"))

decimal = math.fabs(number % 1)

print(decimal)