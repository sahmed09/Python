num = 8668
sum = 0
temp = num

while temp != 0:
    r = temp % 10
    sum = sum * 10 + r
    temp = temp // 10  # temp = int(temp / 10) both are same

if sum == num:
    print("Palindrome")
else:
    print("Not Palindrome")


###################################
def palindrome(x):
    sum = 0
    temp = x
    while temp != 0:
        r = temp % 10
        sum = sum * 10 + r
        temp = temp // 10  # temp = int(temp / 10) both are same

    return sum


num = 8989
g = palindrome(num)
if g == num:
    print("Palindrome")
else:
    print("Not Palindrome")
