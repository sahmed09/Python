a = 2
b = 10
cnt = 0

for i in range(a, b+1):
    if i % 2 == 0:
        cnt += 1

print(cnt)


############################
def even(x, y):
    sum = 0
    for j in range(x, y + 1):
        if j % 2 == 0:
            sum += 1

    return sum


s = even(0, 100)
print(s)
