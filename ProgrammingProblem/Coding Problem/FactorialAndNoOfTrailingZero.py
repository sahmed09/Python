# part 1 - Calculate Factorial of a given Number
# part 2 - Find the number of trailing zeros in that factorial


def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)


# def factorial_trailing_zeros(number):
#     fac = factorial(number)
#     print(fac)
#     count = 0
#     while fac % 10 == 0:
#         count += 1
#         fac = fac/10
#     return count

# we cannot find factorial of a large number like 560.
# To solve this problem, using prime factorization. We just need to find 5. Number of 0 depends on number of 5.
# coz we can find 2 almost every 1 interval. and 5*2=10
# 5! = 5*4*3*2*1
# 6! = 6*5*4*3*2*1
# 100! = 100//5 + 100//5*5

def factorial_trailing_zeros(number):
    count = 0
    i = 5
    while number//i != 0:
        count += number//i
        i = i*5
    return count


if __name__ == '__main__':
    number = int(input("Enter a number: "))

    fact = factorial(number)
    print(f"Factorial is: {fact}")

    print("Number of Trailing zeroes:", factorial_trailing_zeros(number))

