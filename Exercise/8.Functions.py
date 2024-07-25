def even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


even_odd(25)


def even_odd_2(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


val = even_odd_2(24)
print(val)


# first input is positional argument, second input is keyword argument
def hello(name, age=20):
    print('Name {} and age {}'.format(name, age))


hello("Shihab")


# *args -> positional argument, **kwargs -> keyword argument
def hello_2(*args, **kwargs):
    print(args)
    print(kwargs)


hello_2('Shihab', 'Ahmed', age=20, dob=1999)

name = ['Shihab', 'Ahmed']
age = {'age': 20, 'dob': 1999}

hello_2(name, age)  # This is wrong way to write
hello_2(*name, **age)  # This is correct way to write

# Returning multiple outputs
lst = [1, 2, 3, 4, 5, 6, 7]


def even_odd_sum(lst):
    even_sum = 0
    odd_sum = 0
    for i in lst:
        if i % 2 == 0:
            even_sum = even_sum + i
        else:
            odd_sum = odd_sum + i
    return even_sum, odd_sum


even, odd = even_odd_sum(lst)
print(even, odd)
