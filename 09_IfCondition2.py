itemName = input("Enter item name :")

itemPrice = float(input("Enter price of %s :" %itemName))
if itemPrice >= 300:
    discount = itemPrice * 0.05
    itemPrice = itemPrice - discount
print("Price include discount : ",itemPrice)

itemVAT = itemPrice * 0.07
print("VAT : ",itemVAT)

TotalPrice = itemPrice + itemVAT
print("Grand Total : ",TotalPrice)  