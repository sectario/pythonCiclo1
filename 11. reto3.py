amountProducts = int(input("cantidad"))
totalPurchase = 0
totalVat = 0
total = 0
vat = 0
i = 0
codeList = []
nameList = []
ammountList = []
priceList = []
vatList = []
productPriceList = []


def  printResult(productCode, productName, subtotalValue, subtotalVat):
    print(productCode)
    print(productName)
    print(subtotalValue)
    print(subtotalVat)
    

def vatCalculation(subtotalValue):
    if vatType == 1:
        totalValue = 0
        return totalValue
    elif vatType == 2:
        totalValue = subtotalValue * 0.05
        return totalValue
    elif vatType == 3:
        totalValue = subtotalValue * 0.19
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
    totalPurchase = vatCalculation(subtotalValue) + subtotalValue
    totalVat = vatCalculation(subtotalValue)
    codeList.append(productCode)
    nameList.append(productName)
    ammountList.append(amount)
    priceList.append(subtotalValue)
    vatList.append(totalVat)
    productPriceList.append(totalPurchase)
    
    i = i + 1

print(len(codeList))
print(len(nameList))
print(len(ammountList))
print(len(priceList))
print(len(vatList))


for i in range(0, amountProducts):

    print(codeList[i])
    print(nameList[i])
    print(priceList[i])
    print(productPriceList[i])
    total = total + productPriceList[i]
    vat = vat + vatList[i]


print(total)
if vat == 0:
    print(int(vat))
else:
    print(vat)

