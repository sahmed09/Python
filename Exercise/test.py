def add_all(a, b):
    return a + b


while true:
    try:
        inp = float(input('Enter the number: '))
        break
    except ValueError:
        print("Please enter a number")

print(inp)
