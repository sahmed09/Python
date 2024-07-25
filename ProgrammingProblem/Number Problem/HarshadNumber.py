"""Python program to determine whether the given number is a Harshad Number."""
# If a number is divisible by the sum of its digits, then it will be known as a Harshad Number. (8, 54, 120 etc)
# The number 156 is divisible by the sum (12) of its digits (1, 5, 6 )

num = 156
sum = 0

# Make a copy of num and store it in variable n
n = num

# Calculates sum of digits
while n > 0:
    rem = n % 10
    sum = sum + rem
    n = n // 10

print(sum)
# Checks whether the number is divisible by the sum of digits
if num % sum == 0:
    print(num, "is a harshad number")
else:
    print(num, "is not a harshad number")
