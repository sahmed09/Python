import os

# Python os module:
# To delete a file, you must import the OS module, and run its os.remove() function:
# os.remove("d.txt")

# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:
if os.path.exists("d.txt"):
    os.remove("d.txt")
else:
    print("The file does not exist")

# Delete Folder/Directory
# To delete an entire folder, use the os.rmdir() method
# Only empty folders can be removed
# os.rmdir("demo")

# The rename() Method:
# The rename() method takes two arguments, the current filename and the new filename.
# os.rename(current_file_name, new_file_name)
# os.rename("test1.txt", "test2.txt")  # Rename a file from test1.txt to test2.txt
