###########################
num = 9768
sum = 0
temp = num

while temp != 0:
    r = temp % 10
    sum = sum * 10 + r
    temp = int(temp / 10)  # temp = temp // 10 bot are same

print(sum)

########################
x = 9768
x = str(x)[::-1]
print(x)


######################
def my_function(x):
    return x[::-1]


txt = my_function("9768")
print(txt)
