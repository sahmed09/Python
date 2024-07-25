mylist = ["a", "c", "b", "a", "c"]
mylist = list(dict.fromkeys(mylist))  # automatically remove duplicates because dictionaries cannot have duplicate keys.
print(mylist)


# Using Function:
def my_function(x):
    return list(dict.fromkeys(x))


mylist = my_function(["a", "c", "b", "a", "c"])

print(mylist)
