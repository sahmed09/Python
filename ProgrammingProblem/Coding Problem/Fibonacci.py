first = 0
sec = 1
limit = 51

print(first, sec, end=" ")

for i in range(2, limit):
    fib = first + sec
    print(fib, end=" ")
    first = sec
    sec = fib
