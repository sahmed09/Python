import os

# print(dir(os))

print(os.getcwd())  # find current working directory

# os.chdir("C://")  # change current working directory
# print(os.getcwd())
# f = open("Exercise/Health Management/Apu_Diet.txt")  # will raise error

print(os.listdir())  # gives file list of current directory
# print(os.listdir("C://"))  # gives file list of given directory

print(type(os.listdir()))  # check type

# os.mkdir("Hello")  # create directory

# os.makedirs("Hello/Hel")  # create directory under directory

# os.rename("b.txt", "c.txt")  # rename file
# os.rename("Hello", "Hell")

print(os.environ.get('HOME'))  # to read environment variable
print(os.environ.get('Path'))

print(os.path.join("C:/", "Hello.txt"))  # Joins two path
print()

print(os.path.exists("E://PycharmProjects"))  # returns if a path is exists or not
print(os.path.exists("E://PycharmProjects/Practice/Hello"))
print()

print(os.path.isfile("E://PycharmProjects"))  # returns if it's a file or not
print(os.path.isfile("E://PycharmProjects/Practice/Arrays.py"))

print(os.path.isdir("E://PycharmProjects"))  # returns if it's a directory or not
print(os.path.isdir("E://PycharmProjects/Practice/Arrays.py"))
