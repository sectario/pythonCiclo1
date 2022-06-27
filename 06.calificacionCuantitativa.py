amountProducts = int(input("cantidad"))
totalPurchase = 0
totalVat = 0
i = 0

def  printResult(productCode, productName, subtotalValue, subtotalVat):
    print(productCode)
    print(productName)
    print(subtotalValue)
    print(subtotalVat)
    

def vatCalculation(subtotalValue):
    if vatType == 1:
        totalValue = subtotalValue
        return totalValue
    elif vatType == 2:
        totalValue = subtotalValue * 1.05
        return totalValue
    elif vatType == 3:
        totalValue = subtotalValue * 1.19
        return totalValue
    else:
        return 0


while i < amountProducts:
    productCode = int(input("code"))
    productName = str(input("name"))
    amount = float(input("cantidad"))
    unitValue = float(input("valor unitario"))
    vatType = int(input("iva"))
    subtotalValue = amount * unitValue
    totalPurchase = totalPurchase + vatCalculation(subtotalValue)
    totalVat = totalVat + vatCalculation(subtotalValue) - subtotalValue
    printResult(productCode, productName, subtotalValue, vatCalculation(subtotalValue))
    i = i + 1


print(totalPurchase)
if totalVat == 0:
    print(int(totalVat))
else:
    print(totalVat)

