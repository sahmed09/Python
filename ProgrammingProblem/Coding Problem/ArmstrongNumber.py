num = 371
sum = 0
temp = num

while temp != 0:
    r = temp % 10
    sum = sum + r * r * r
    temp = int(temp / 10)  # temp = temp // 10 bot are same

if sum == num:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")


###################################
def armstrong(x):
    sum = 0
    temp = x
    while temp != 0:
        r = temp % 10
        sum = sum + r * r * r
        temp = int(temp / 10)  # temp = temp // 10 bot are same

    return sum


num = 154
g = armstrong(num)
if g == num:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")
