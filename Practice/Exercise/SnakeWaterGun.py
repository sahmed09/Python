import random

choices = ['s', 'w', 'g']
chance = 10
computer_score = 0
human_score = 0

while chance != 0:
    human_choice = input("Enter s/w/g for snake, water or gun : ").lower()

    if human_choice in choices:
        computer_choice = random.choice(choices)
        chance -= 1

        if human_choice == computer_choice:
            print("Draw!")

        elif computer_choice == 's' and human_choice == 'w':
            print(f"Computer Win with choice {computer_choice}")
            computer_score += 1

        elif computer_choice == 'w' and human_choice == 'g':
            print(f"Computer Win with choice {computer_choice}")
            computer_score += 1

        elif computer_choice == 'g' and human_choice == 's':
            print(f"Computer Win with choice {computer_choice}")
            computer_score += 1

        else:
            print(f"You Win and Computer choice was {computer_choice}")
            human_score += 1
        print(f"{chance} chances left!\n")

    else:
        print("Wrong Entry. Please Enter Correct Choice.")
        print(f"{chance} chances left!\n")

if computer_score > human_score:
    print(f"Computer Win with gaining {computer_score} points")
elif computer_score < human_score:
    print(f"You Win with gaining {human_score} points")
else:
    print("Draw the game!")
