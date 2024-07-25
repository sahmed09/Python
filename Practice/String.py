# Multiline Strings
a = """Lorem 
ipsum
Doller Site"""
print(a)

a = '''Lorem 
ipsum
Doller Site'''
print(a)

b = "Hello, World!"
print("length = ", len(b))  # len() method returns length of string

# Strings are Arrays
print(b[1])
print(b[4])

# Slicing
print(b[2:5])
print(b[3:8])
print(b[::])  # print full string [::] -> [0:length:1]
print(b[:])

# Negative Indexing
print(b[-5:-2])
print(b[-6:-2])
print(b[::-2])

# String Methods
c = " Hello, World! "
print(c.strip())  # strip() method removes any whitespace from the beginning or the end
print(b.lower())  # lower() method returns the string in lower case
print(b.upper())  # upper() method returns the string in upper case
print(b.replace("H", "J"))  # replace() method replaces a string with another string
print(b.split(","))  # split() method splits the string into substrings if it finds instances of the separator
print(b.count("o"))  # Returns the number of times a specified value occurs in a string
c = " Hello, World! "
print(c.lstrip())  # lstrip() method removes any whitespace from the beginning
print(c.rstrip())  # rstrip() method removes any whitespace from the end

# Check String or "in" operator
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print("ain" in txt)
print(x)
y = "ain" not in txt
print(y)

# String Concatenation
c = "Hello"
d = "World!"
print(c + " " + d)

# String Format
age = 36
txt = "My name is John, I am {}"
print(txt.format(age))  # format() method to insert numbers into strings
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
quantity = 3
itemno = 567
price = 49.95

print("I want {quantity} pieces of item {itemno} for {price} dollars.".format(quantity=quantity, itemno=itemno,
                                                                              price=price))
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Escape Character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Updating Strings
var = "Hello World"
print("Updated String : ", var[:6] + "Python")
print()

# Triple Quotes:
# Python's triple quotes comes to the rescue by allowing strings to span multiple lines,
# including verbatim NEWLINEs, TABs, and any other special characters.
para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print(para_str)
print()

# Unicode String
print(u'Hello, world!')

h = "hello world"
print(h.isalnum())
print(h.isalpha())
print(h.endswith("world"))
print(h.count('l'))
print(h.capitalize())  # Capitalize first letter
print(h.find("world"))

# join() function:
lis = ["Apple", "Banana", "Mango", "Orange", "Guava"]
for item in lis:
    print(item, "and", end=" ")
print("other fruits.")

lis = ["Apple", "Banana", "Mango", "Orange", "Guava"]
a = " and ".join(lis)
print(a, "and other fruits.")
a = ", ".join(lis)
print(a, "and other fruits.")

x = "stuff"
print(dir(x))  # shows the functions available for the string

# String comparison:
word = 'banana'
if word == 'banana':
    print('All right, bananas.')

word = "Pineapple"
if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')

# Parsing strings:
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos + 1:sppos]
print(host)

print(ord('H'))  # ord() function tells us the numeric value of a simple ASCII character
print(ord('h'))
print(type(b'abc'))
