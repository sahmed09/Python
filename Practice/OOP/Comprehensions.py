# List comprehension:
ls = []
for i in range(100):
    if i % 3 == 0:
        ls.append(i)
print(ls)  # Without List comprehension
ls = [i for i in range(100) if i % 3 == 0]  # List comprehension
print(ls)
print()

# Dictionary comprehension:
dict1 = {i: f"item{i}" for i in range(1, 10) if i % 2 == 0}  # Dictionary comprehension
print(dict1)
dict2 = {value: key for key, value in dict1.items()}  # Reversing key, value
print(dict2)
print()
dict1 = {'a': 45, 'b': 65, 'A': 5}
print({k.lower(): dict1.get(k.lower(), 0) + dict1.get(k.upper(), 0) for k in dict1.keys()})
print()

# Set comprehension:
dresses = {dress for dress in ["dress2", "dress3", "dress2", "dress3"]}
print(dresses)  # Set comprehension
print(type(dresses))
squared = {x**2 for x in [1, 2, 3, 4, 4, 4, 4, 5, 5, 5, 5]}
print(squared)
print()

# Generator comprehension:
evens = (i for i in range(50) if i % 2 == 0)  # Generator comprehension
print(type(evens))
print(evens)
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
for item in evens:
    print(item, end=" ")
print()
