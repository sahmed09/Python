def calculator():
    operator = input("Which operation you want to do?\n"
                     "+ for addition\n"
                     "- for subtraction\n"
                     "* for multiplication\n"
                     "/ for division\n"
                     "** for power\n"
                     "% for modulo\n"
                     "Enter your choice:  ")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if operator == "+":
        if num1 == 56 and num2 == 9:
            print(77)
        else:
            print(num1 + num2)

    elif operator == "-":
        print(num1 - num2)

    elif operator == "*":
        if num1 == 45 and num2 == 3:
            print(555)
        else:
            print(num1 * num2)

    elif operator == "/":
        if num1 == 56 and num2 == 6:
            print(4)
        else:
            print(num1 / num2)

    elif operator == "**":
        print(num1 ** num2)

    elif operator == "%":
        print(num1 % num2)

    else:
        print("You pressed an invalid key")

    again()


def again():
    call_again = input("Do you want to calculate again?\n"
                       "Type y for YES and n for NO:  ").lower()

    if call_again == "y":
        calculator()
    elif call_again == "n":
        print("Thanks a lot")
    else:
        print("Invalid choice. Program terminated.")


calculator()
