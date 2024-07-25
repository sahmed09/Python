# Using with statement to open files: (no need to close the file while using with)
with open("demofile.txt", 'r') as f:
    content = f.read()
    print(content)
print()

with open("demofile.txt") as f:
    content = f.read(20)  # Read first 20 characters
    print(content)
print()

# File Pointer positions:
# Python provides the tell() method which is used to print the byte number at which the file pointer exists.
fileptr = open("demofile.txt", "r")  # open the file file2.txt in read mode

print("The filepointer is at byte :", fileptr.tell())  # initially the filepointer is at 0

content = fileptr.read()  # reading the content of the file

# after the read operation file pointer modifies. tell() returns the location of the fileptr.
print("After reading, the filepointer is at:", fileptr.tell())
fileptr.close()
print()

# Modifying file pointer position:
# the python provides us the seek() method which enables us to modify the file pointer position externally.
# <file-ptr>.seek(offset[, from)
# The seek() method accepts two parameters:
# offset: It refers to the new position of the file pointer within the file.
# from: It indicates the reference position from where the bytes are to be moved.
fileptr = open("demofile.txt", "r")  # open the file file2.txt in read mode

print("The filepointer is at byte :", fileptr.tell())  # initially the filepointer is at 0

fileptr.seek(10)  # changing the file pointer location to 10.

print("After reading, the filepointer is at:", fileptr.tell())  # tell() returns the location of the fileptr.
fileptr.close()
