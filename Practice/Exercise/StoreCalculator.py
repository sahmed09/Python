# Write a python program which will keep adding a stream of numbers inputted by the user. The adding stops
# as soon as user presses q key on the keyboard.

sum = 0
name = input("Enter your name: ")
shopping = {}
i = 0
while True:
    user_input = input("Enter the item price or press q to Quit: ")
    if user_input != 'q':
        sum = sum + float(user_input)
        print(f"Your bill so far {sum}\n")
        shopping[f"item {i}"] = user_input
        i += 1
    else:
        # print(f"Your total bill is {sum}. Thanks for shopping.\n")
        break
print()

with open("Shopping.txt", "w") as f:
    f.write("Shihab Enterprise\n")
    f.write(f"Recipient : {name}\n")
    for key, value in shopping.items():
        f.write(key + " : " + value + "\n")
    f.write(f"Your total bill is {sum}. Thanks for shopping.")

# for key, value in shopping.items():
#     print(key + " : " + value)

with open("Shopping.txt", "r") as f:
    content = f.read()
print(content)

# Receipt Printer
