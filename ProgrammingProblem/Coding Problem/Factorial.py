num = 8
fact = 1

for i in range(num, 1, -1):
    fact = fact * i

if num < 0:
    print("Sorry, factorial does not exists of negative numbers.")
else:
    print("The factorial of", num, "is", fact)
