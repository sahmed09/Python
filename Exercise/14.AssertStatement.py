"""Python provides the assert statement to check if a given logical expression is true or false. Program execution
proceeds only if the expression is true and raises the AssertionError when it is false."""

# num = 10
# assert num > 10

try:
    num = int(input("Enter the even number: "))
    assert num % 2 == 0
    print("The number is even")
except AssertionError:
    print("Please enter even number")
