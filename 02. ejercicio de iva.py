productCode = int(input())
productName = str(input())
amount = int(input())
unitValue = int(input())

subtotalValue = float(amount * unitValue)

totalValue = subtotalValue * 1.19

# print("Codigo del producto ", productName, ": ", productCode, "\nValor si IVA: ",subtotalValue, "\nValor con IVA: ", totalValue)

# print(productCode, "\n", productName, "\n", subtotalValue, "\n", totalValue)

print(productCode)
print(productName)
print(subtotalValue)
print(totalValue)