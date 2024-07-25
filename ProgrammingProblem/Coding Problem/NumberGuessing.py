import random

x = random.randrange(1, 5)

guess = int(input("Enter a number within 5 : "))

if x == guess:
    print("Congratulations! Correct Guess")
else:
    print("Sorry! Incorrect guess")
    print("Correct Number was ", x)
