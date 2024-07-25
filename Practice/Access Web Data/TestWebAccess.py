import re

# Sample Data:
hand = open("sample_data.txt")
numlist = list()

for line in hand:
    line = line.rstrip()
    # print(line)
    stuff = re.findall('([0-9]+)', line)  # finding all the numbers
    # print(stuff)
    if len(stuff) == 0:
        continue
    # print(stuff)
    for num in stuff:
        num = int(num)
        numlist.append(num)  # appending all the lists in one list
print(numlist)
print(len(numlist))
print(sum(numlist))
hand.close()
print()

# Actual Data:
hand = open("actual_data.txt")
numlist = list()

for line in hand:
    line = line.rstrip()
    # print(line)
    stuff = re.findall('([0-9]+)', line)  # finding all the numbers
    # print(stuff)
    if len(stuff) == 0:
        continue
    # print(stuff)
    for num in stuff:
        num = int(num)
        numlist.append(num)  # appending all the lists in one list
print(numlist)
print(len(numlist))
print(sum(numlist))
hand.close()

# For shortcut
# print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
