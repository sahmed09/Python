m = 100
n = 500


def armstrong(x):
    sum = 0
    temp = x
    while temp != 0:
        r = temp % 10
        sum = sum + r * r * r
        temp = int(temp / 10)  # temp = temp // 10 bot are same

    return sum


for num in range(m, n+1):
    result = armstrong(num)
    if num == result:
        print(result)
