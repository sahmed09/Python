# sumOfDigits() Calculates the sum of squares of digits
def sumOfDigits(num):
    sum = 0

    while num > 0:
        rem = num % 10
        sum = sum + rem*rem
        num = num//10
    return sum


# isHappyNumber() will determine whether a number is happy or not
def isHappyNumber(x):
    # Happy number always ends with 1 and
    # unhappy number ends in a cycle of repeating numbers which contains 4
    while x != 1 and x != 4:
        x = sumOfDigits(x)

    return x


# Displays all happy numbers between 1 and 100
print("List of happy numbers between 1 and 100: ")
for i in range(1, 101):
    result = isHappyNumber(i)

    if result == 1:
        print(i, end=" ")
