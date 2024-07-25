"""Python program to check if the given number is a Disarium Number"""
# A number is said to be the Disarium number,
# when the sum of its digit raised to the power of their respective positions becomes equal to the number itself.
# 1^1+ 7^2 + 5^3 = 1+ 49 + 125 = 175


# calculateLength() will count the digits present in a number
def calculateLength(n):
    length = 0
    while n != 0:
        length += 1
        n = n // 10
    return length


num = 175
sum = 0
len = calculateLength(num)
# print(len)

# Makes a copy of the original number num
x = num

# Calculates the sum of digits powered with their respective position
while x > 0:
    rem = x % 10
    sum = sum + int(rem**len)
    x = x // 10
    len = len - 1

# Checks whether the sum is equal to the number itself
if sum == num:
    print(num, " is a disarium number")
else:
    print(num, " is not a disarium number")
