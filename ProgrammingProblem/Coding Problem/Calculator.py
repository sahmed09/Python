def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "You can't divide by zero!"


print("Select Operation : ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice(1/2/3/4) : "))

if choice < 1 or choice > 4:
    print("Enter a valid number")
else:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    if choice == 1:
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == 2:
        print(num1, "-", num2, "=", sub(num1, num2))
    elif choice == 3:
        print(num1, "*", num2, "=", mul(num1, num2))
    elif choice == 4:
        print(num1, "/", num2, "=", div(num1, num2))
