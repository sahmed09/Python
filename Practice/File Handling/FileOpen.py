# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:
"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"""
# In addition one can specify if the file should be handled as binary or text mode
"""
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
"+" - Read and write both
"""

# Syntax
# To open a file for reading it is enough to specify the name of the file:
# f = open("demo.txt")

# The code above is the same as:
f = open("demo.txt", "rt")  # Here "f" is a handle and it is a connection to the file's data
print(f)

# Because "r" for read, and "t" for text are the default values, no not need to specify them.

# The mkdir() Method:
# You can use the mkdir() method of the os module to create directories in the current directory.
# import os
# os.mkdir("newdir")  # Create a directory "test"

# The chdir() Method:
# You can use the chdir() method to change the current directory.
# import os
# os.chdir("/home/newdir")  # Changing a directory to "/home/newdir"

# The getcwd() Method:
# The getcwd() method displays the current working directory.
# import os
# os.getcwd()  # This would give location of the current directory
