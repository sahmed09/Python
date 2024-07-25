import random


def guess_game(a, b, actual):
    guess = int(input(f"Guess a number between {a} and {b} : "))
    nguess = 1

    while guess != actual:
        if guess < actual:
            guess = int(input("Enter a bigger number : "))
            nguess += 1
        else:
            guess = int(input("Enter a smalle number : "))
            nguess += 1

    print(f"You guess the number in {nguess} guesses\n")
    return nguess


if __name__ == '__main__':
    a = int(input("Enter the value of a : "))
    b = int(input("Enter the value of b : "))

    guess1 = random.randint(a, b)
    print("\nPlayer 1's turn : ")
    player1 = guess_game(a, b, guess1)

    guess2 = random.randint(a, b)
    print("Player 2's turn : ")
    player2 = guess_game(a, b, guess2)

    if player1 < guess2:
        print("Player 1 won the match!\n")

    elif player1 > player2:
        print("Player 2 won the match!\n")

    else:
        print("It's a tie\n")

    print(f"The number for Player 1 was {guess1} and for Player 2 was {guess2}")
