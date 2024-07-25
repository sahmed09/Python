def recur_factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)


num = 8

if num < 0:
    print("Sorry, factorial does not exists of negative numbers.")

else:
    print("The factorial of", num, "is", recur_factorial(num))
