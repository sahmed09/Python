x = 8975
sum = 0
temp = x

while temp != 0:
    r = temp % 10
    sum = sum + r
    temp = int(temp / 10)

print(sum)

x = 8975
x = str(x)
summ = 0
for digit in x:
    summ = summ + int(digit)

print(summ)
