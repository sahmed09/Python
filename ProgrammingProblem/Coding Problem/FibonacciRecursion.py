def recur_fib(n):
    if n <= 1:
        return n
    else:
        return recur_fib(n-1) + recur_fib(n-2)


num = 10

if num <= 0:
    print("Please Enter a positive number")
else:
    print("Fibonacci Sequence:")
    for i in range(num):
        print(recur_fib(i), end=" ")
