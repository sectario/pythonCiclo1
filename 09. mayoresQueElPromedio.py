print("Cuantos numeros desea ingresar? \n")


numbersList = []

ammountData = int(input())




i= 0
suma = 0

while ammountData > len(numbersList):
    agddItem = numbersList.append(int(input("Nùmero " )))
    

while i < len(numbersList):
    suma = suma + numbersList[i]
    i = i + 1

average = suma / len(numbersList)

i = 0

while i < len(numbersList):
    if numbersList[i] > average:
        print(numbersList[i])

    i = i + 1
    