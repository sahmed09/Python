"""Python program to check if the given number is Happy Number"""
# A number is said to be happy if it yields 1 when replaced by the sum of squares of its digits repeatedly.
# If this process results in an endless cycle of numbers containing 4, then the number will be an unhappy number.
# 32 -> 3^2+ 2^2 = 13 -> 1^2 + 3^2 = 10 -> 1^2 + 0^2 = 1
# Some Happy numbers are 7, 28, 100, 320, etc


# isHappyNumber() will determine whether a number is happy or not
def isHappyNumber(num):
    sum = 0

    # Calculates the sum of squares of digits
    while num > 0:
        rem = num % 10
        sum = sum + rem*rem
        num = num//10
    return sum


num = 82
result = num

while result != 1 and result != 4:
    result = isHappyNumber(result)

# Happy number always ends with 1
if result == 1:
    print(num, "is a happy number")
# Unhappy number ends in a cycle of repeating numbers which contain 4
elif result == 4:
    print(num, "is not a happy number")
