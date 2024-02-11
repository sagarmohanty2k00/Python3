import math

bp = float(input("Buying price: "))
sp = float(input("Selling price: "))

print("Profit: ", math.floor(((sp - bp)/bp)*100), "%")
print("Profit: ", round(((sp - bp)/bp)*100), "%")
print("Profit: ", (((sp - bp)/bp)*100), "%")