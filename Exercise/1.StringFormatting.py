# The format() method allows you to format selected parts of a string.
# Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?
# To control such values, add placeholders (curly brackets {}) in the text, and run the values through format() method

# String format()
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

# add parameters inside the curly brackets to specify how to convert the value
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# Multiple Values
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

print("I want {quantity} pieces of item {itemno} for {price} dollars.".format(quantity=quantity, itemno=itemno,
                                                                              price=price))

# Index Numbers
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# Named Indexes
# also use named indexes by entering a name inside the curly brackets {carname},
# but then must use names when pass the parameter values txt.format(carname = "Ford"):
myorder = "I have a {carname}. It is a {model}"
print(myorder.format(carname="Ford", model="Mustang"))

quantity = 3
itemno = 567
myorder = "I want %s pieces of item number %s " % (quantity, itemno)
print(myorder)

# f-string:
quantity = 3
itemno = 567
myorder = f"I want {2*quantity} pieces of item number {itemno}"
print(myorder)


# Using Function
def greeting(name):
    return "Hello {}.".format(name)


greet = greeting('Shihab')
print(greet)


def welcome_email(fname, lname):
    return "Welcome {} {}.".format(fname, lname)


wel = welcome_email('Shihab', 'Ahmed')
print(wel)


def welcome(fname, lname):
    return "Welcome {fname} {lname}.".format(lname=lname, fname=fname)


wel = welcome('Shihab', 'Ahmed')
print(wel)
