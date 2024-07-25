lst1 = ["Shihab", "Ahmed", "Shihab2"]
lst2 = ["Shihab", "Ahmed", "Shihab2"]
print('lst1 == lst2:', lst1 == lst2)

a = "Shihab"
b = "Shihab"
print('a == b:', a == b)
print()

print('lst1:', lst1, 'lst2:', lst2)
print('lst1 is lst2:', lst1 is lst2)
print()

lst1 = ["Shihab", "Ahmed", "Shihab2"]
lst2 = lst1
print('lst1:', lst1)
print('lst2:', lst2)
print('lst1 is lst2:', lst1 is lst2)
print('lst2 is lst1:', lst2 is lst1)
print()

lst2[0] = 'Shihab2'
print('lst1:', lst1)
print('lst2:', lst2)
