amountProducts = int(input("cantidad"))
totalPurchase = 0
totalVat = 0
total = 0
vat = 0
i = 0

purchaseList = []

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
    purchaseList.append(
        {
            'productCode': productCode,
            'productName': productName,
            'ammountList': amount,
            'subtotalValue': subtotalValue,
            'totalVat': totalVat,
            'totalPurchase': totalPurchase
            })
    i = i + 1


def organizeDiccionaryList(diccionaryList):
    organize = sorted(diccionaryList, key=lambda d: d['productName'])
    return organize

purchaseList = organizeDiccionaryList(purchaseList)

for i in range(0, amountProducts):

    print(purchaseList[i]['productCode'])
    print(purchaseList[i]['productName'])
    print(purchaseList[i]['subtotalValue'])
    print(purchaseList[i]['totalPurchase'])
    total = total + purchaseList[i]['totalPurchase']
    vat = vat + purchaseList[i]['totalVat']


print(total)
if vat == 0:
    print(int(vat))
else:
    print(vat)