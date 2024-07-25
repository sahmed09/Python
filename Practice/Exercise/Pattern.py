try:
    inp = int(input("How many rows you want to print? "))
    num = int(input("Input 1 or 0: "))
    typ = bool(num)

    if inp < 0:
        print("You have entered negative number")
    else:
        if typ:
            for i in range(inp):
                for j in range(i + 1):
                    print("*", end=" ")
                print()
        else:
            for i in range(inp, 0, -1):
                for j in range(i):
                    print("*", end=" ")
                print()
except Exception as e:
    print(e)

try:
    inp = int(input("Enter the number: "))

    if inp < 0:
        print("You have entered negative number")
    else:
        for i in range(1, inp + 1):
            count = 0
            for j in range(i):
                if j == 0 or j == i - 1:
                    print(chr(65 + count), end=" ")
                    count += 1
                else:
                    if i != inp:
                        print(" ", end=" ")
                    else:
                        print(chr(65 + count), end=" ")
                        count += 1
            print()
except Exception as e:
    print(e)
