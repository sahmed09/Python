m = 10
n = 50
cnt = 0
total = 0

for i in range(m, n+1):
    for j in range(2, i):
        if i % j == 0:
            cnt += 1
            break

    if cnt == 0:
        total += 1

    cnt = 0

if m > 1:
    print("Total Prime number = ", total)
else:
    print("Total Prime number = ", total-1)


a = 10
b = 50
for num in range(a, b+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
