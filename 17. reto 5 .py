amountProducts = int(input("cantidad"))
totalPurchase = 0
totalVat = 0
total = 0
vat = 0
i = 0

purchaseList = []
articulos={1:"Lapiz",2:"Cuaderno",3:"Borrador",4:"Regla",5:"ColoresX12",6:"Escuadra",7:"Calculadora",8:"CrayonesX6"}
precios={1:2500,2:4500,3:1500,4:5000,5:24000,6:4700,7:45000,8:8900}

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
    amount = float(input("cantidad"))
    vatType = int(input("iva"))
    unitValue = precios[productCode]
    productName = articulos[productCode]
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
    organize = sorted(diccionaryList, key=lambda p: p['productCode'])
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