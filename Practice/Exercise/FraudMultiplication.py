import random


def rohan_multiplication(number):
    wrong = random.randint(0, 9)
    # print(wrong)
    table = [i * number for i in range(1, 11)]
    table[wrong] = table[wrong] + random.randint(0, 10)
    # print(table[wrong])
    return table


def is_correct(table, number):
    for i in range(1, 11):
        if table[i-1] != i * number:
            return i-1

    return None


if __name__ == '__main__':
    # print(rohan_multiplication(8))
    num = int(input("Enter a number : "))
    myTable = rohan_multiplication(num)
    print(myTable)
    wrongIndex = is_correct(myTable, num)
    if wrongIndex is None:
        print("The table is fully OK")
    else:
        print(f"The table is wrong at index {wrongIndex}")
