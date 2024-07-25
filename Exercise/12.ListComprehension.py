"""List comprehension offers a concise way to create a new list based on the values of an existing list.
It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The
expressions can be anything, meaning you can put in all kinds of objects in lists."""

lst1 = []


def lst_square(lst):
    for i in lst:
        lst1.append(i * i)
    return lst1


res = lst_square([1, 2, 3, 4, 5, 6, 7])
print(res)

# List Comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = [num * num for num in numbers]
print(result)

result = [num * num for num in numbers if num % 2 == 0]
print(result)

result = [num * num for num in numbers if num % 2 != 0]
print(result)
