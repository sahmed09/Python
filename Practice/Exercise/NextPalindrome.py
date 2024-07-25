def next_palindrome(n):
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':
    n = int(input("Enter the number of test cases: "))
    numbers = []
    for i in range(n):
        number = int(input("Enter the number : "))
        numbers.append(number)
    print(f"Entered List : {numbers}")

    for i in range(n):
        if is_palindrome(numbers[i]) is True:
            print(f"{numbers[i]} is a palindrome number.")
        else:
            print(f"Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")

    print(f"Output list : {[numbers[i] if numbers[i] < 10 else next_palindrome(numbers[i]) for i in range(n)]}")
