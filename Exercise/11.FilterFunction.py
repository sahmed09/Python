def even(num):
    if num % 2 == 0:
        return True


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

result = list(filter(even, lst))
print(result)


result = list(filter(lambda num: num % 2 == 0, lst))  # filter() will filter only the numbers which are true
print(result)

result = list(map(lambda num: num % 2 == 0, lst))
print(result)  # map() will return all the numbers as True or False based on the condition
