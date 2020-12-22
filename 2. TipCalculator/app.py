# This project is based on operators ^_^

print("Welcome to the Tip Calculator!")

bill = float(input("what was the total bill? $"))
percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))/100 + 1.0
people = int(input("How many people to split the bill? "))

totalBill = bill * percentage
billPerPerson = round(totalBill / people, 2)

print(f"Each person should pay: ${billPerPerson}")