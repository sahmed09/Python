# To open the file, use the built-in open() function.
# The open() function returns a file object, which has a read() method for reading the content of the file
print("Read Full file : ")
f = open("demofile.txt", "r")  # Here "f" is a handle and it is a connection to the file's data
print(f)
content = f.read()  # returns full file
print(content)
f.close()
print()

# Read Only Parts of the File
# By default the read() method returns the whole text, but can also specify how many characters want to return:
print("Read specified character : ")
f = open("demofile.txt", "r")
print(f.read(5))  # returns only "Hello"
f.close()
print()

# Read Lines
# You can return one line by using the readline() method:
print("Read first line : ")
f = open("demofile.txt", "r")
print(f.readline())  # returns the first line
f.close()
print()

# By calling readline() two times, you can read the two first lines:
print("Read first and second line : ")
f = open("demofile.txt", "r")
print(f.readline())  # returns the first line
print(f.readline())  # returns the second line
f.close()

# By looping through the lines of the file, you can read the whole file, line by line:
print("Read full file by looping : ")
f = open("demofile.txt", "r")
for line in f:
    print(line, end="")
f.close()
print("\n")

# Close Files
# It is a good practice to always close the file when you are done with it.
print("Close file : ")
f = open("demofile.txt", "r")
print(f.readline())
f.close()
print()

#
f = open("demofile.txt", "r")
print(f.readlines())
print()

f = open("demofile.txt", "r")
for line in f:
    print(line.rstrip())  # rstrip() considers \n as a whitespace and removes it
f.close()
