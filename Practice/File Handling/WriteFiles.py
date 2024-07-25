# To write to an existing file, you must add a parameter to the open() function:
"""
"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
"""

# File Write
print("File write : ")
"""f = open("demofile2.txt", "a")
f.write("\nNow the file has more content!")
f.close()"""

f = open("demofile2.txt", "r")  # open and read the file after the appending:
print(f.read())
f.close()
print()

# File overwrite
print("File overwrite : ")
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

f = open("demofile3.txt", "r")  # open and read the file after the appending:
print(f.read())
f.close()
print()

# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:
"""
"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist
"""
# f = open("myfile.txt", "x")  # a new empty file is created!, returns an error if the file exist
# f = open("myfile.txt", "w")  # Create a new file if it does not exist, returns an error if the file exist
# f = open("myfile.txt", "a")  #  create a file if it does not exist.

"""f = open("demo.txt", "r+")
print(f.read())
f.write("Thank You")
f.close()"""
