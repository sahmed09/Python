guess = 5
winning_number = 20

print("This is a number guessing game.")
print("Your number is between 1 to 100. You will get 5 chances.")

game_over = False

while not game_over and guess != 0:
    inp = int(input("Guess your number: "))
    guess = guess - 1
    if winning_number == inp:
        print("\nCongratulations! You guess the correct number.")
        game_over = True
        break
    else:
        if winning_number > inp:
            print("\nYou guess too low. Increase your guess.")
        else:
            print("\nYou guess too high. Decrease your guess.")
        print(guess, "guesses left.")

        if guess == 0:
            print("Game Over!")
