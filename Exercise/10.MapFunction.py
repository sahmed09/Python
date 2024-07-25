def even_or_odd(num):
    if num % 2 == 0:
        return "The number {} is Even".format(num)
    else:
        return "The number {} is Odd".format(num)


number = even_or_odd(29)
print(number)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 24, 56, 79]
result = list(map(even_or_odd, lst))
print(result)
