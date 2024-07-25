# size = int(input("Enter size of the list :"))
print("Enter the numbers of the list one by one:")
mylist = [2,3,5,6,7]
# for i in range(size):
#     mylist.append(int(input("Enter list element : ")))

print(f"Your list is {mylist} \n")

# reverse1 = mylist[:]  # making copy of mylist
# reverse1 = list(mylist)  # making copy of mylist
reverse1 = mylist.copy()
reverse1.reverse()
print(f"First Reversed list of {mylist} is {reverse1} \n")

reverse2 = mylist[::-1]
print(f"Second Reversed list of {mylist} is {reverse2} \n")

reverse3 = mylist.copy()
for i in range(len(reverse3)//2):
    reverse3[i], reverse3[len(reverse3)-i-1] = reverse3[len(reverse3)-i-1], reverse3[i]

print(f"Third Reversed list of {mylist} is {reverse3}\n")

if reverse1 == reverse2 and reverse2 == reverse3:
    print("All three method gives same results.")
