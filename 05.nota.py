nota1 = int(input("Nota 1"))
nota2 = int(input("Nota 2"))
notaLab = int(input("Nota laboratorio"))

nota3 = 3 * (60 - (notaLab * 0.3) - (nota1 + nota2) * (0.7 / 3) ) / 7


print(nota3)