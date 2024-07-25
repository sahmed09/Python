# Python has two primitive loop commands:
# while loops
# for loops

# while loop
print("while loop:")
i = 1
while i < 6:
    print(i, end=" ")
    i += 1

# The break Statement
print("\n\nbreak Statement:")
i = 1
while i < 6:
    print(i, end=" ")
    if i == 3:
        break
    i += 1

# The continue Statement
print("\n\ncontinue Statement:")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i, end=" ")

# The else Statement
print("\n\nThe else Statement")
i = 1
while i < 6:
    print(i, end=" ")
    i += 1
else:
    print("\ni is no longer less than 6")

# for loop
print("\nfor loop:")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Looping Through a String
print("\nLooping Through a String")
for x in "Banana":
    print(x)

# The break Statement
print("\nbreak Statement")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
for x in fruits:
    if x == "banana":
        break
    print(x)

# The continue Statement
print("\ncontinue Statement")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# The range() Function
print("\nThe range() function")
for x in range(6):  # 0 to 5
    print(x, end=" ")
print()
for x in range(2, 6):  # 2 to 5
    print(x, end=" ")
print()
for x in range(2, 30, 3):  # 2 to 29 with a increment of 3
    print(x, end=" ")
print()

# Else in For Loop
print("\nElse in For Loop")
for x in range(6):
    print(x, end=" ")
else:
    print("\nFinally Finished!")

k = [3, 6, 9]
for i in k:
    if i == 8:
        print(9)
        break
else:
    print("Not found")

# Nested Loops
print("\nNested Loops")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

# The pass Statement
"""for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error. 
"""
print("\nThe pass Statement:")
for x in [0, 1, 2]:
    pass

for letter in "python":
    if letter == "h":
        pass
        print("This is pass block")
    print("Current letter : ", letter)
print("Good bye!")
print()

ll = [1, 2, 3, 4, 5]
flag = 0
for i in ll:
    print("Current element:", i, end=" ")
    if i == 3:
        pass
        print("\nWe are inside pass block\n")
        flag = 1
    if flag == 1:
        print("\nCame out of pass\n")
        flag = 0
print()
print()

i = 1
# n = int(input("Enter the number up to which you want to print the natural numbers?"))
n = 10
for i in range(0, 10):
    print(i, end=' ')

# n = int(input("Enter the number of rows you want to print?"))
n = 6
i, j = 0, 0
for i in range(0, n):
    print()
    for j in range(0, i+1):
        print("*", end="")
print()

# Infinite while loop:
"""while 1:
    print("Hi! we are inside the infinite while loop")"""

for x in range(30, 2, -3):  # 2 to 29 with a increment of 3
    print(x, end=" ")
print()

ll = [1, 2, 3, 4, 5]
print(6 not in ll)
print(5 not in ll)

fruits = [["apple", ], ["banana"], ["cherry"]]
