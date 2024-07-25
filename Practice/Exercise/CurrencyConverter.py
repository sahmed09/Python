# https://www.x-rates.com/table/?from=INR&amount=1
with open("CurrencyData.txt") as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

# print(currencyDict)

amount = float(input("Enter the amount: "))

print("Enter the name of currency you want to convert this amount to? Available options: \n")
[print(item) for item in currencyDict.keys()]

currency = input("\nPlease enter one of this options: ")
print(f"{amount} INR is equal to {amount * float(currencyDict[currency])} {currency}")
