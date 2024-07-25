import mymodule  # user created module
import platform  # built in module

# A file containing a set of functions you want to include in your application. same as code library.

# Create a Module
# To create a module just save the code you want in a file with the file extension .py

# Use a Module
# we can use the module by using the import statement
# When using a function from a module, use the syntax: module_name.function_name.
mymodule.greeting("Shihab")

# Variables in Module
# The module can contain functions, but also variables of all types (arrays, dictionaries, objects etc)
a = mymodule.person1["age"]
print(a)

# Naming a Module
# module file name can be anything, but it must have the file extension .py

# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword
"""
import mymodule as mx
a = mx.person1["age"]
print(a)
"""

# Loading the module in our python code:
# The import statement
# The from-import statement

# Built-in Modules
# import platform is a built in module
x = platform.system()
print(x)
print()

# Using the dir() Function
# The dir() function is a built-in function to list all the function names (or variable names) in a module.
x = dir(platform)
print(x)
print()

# Import From Module
# import only parts from a module, by using the from keyword.
"""
from mymodule import person1
print(person1["age"])
"""
# When importing using the from keyword, do not use the module name when referring to elements in the module.
# Example: person1["age"], not mymodule.person1["age"]

# The reload() function:
# a module is loaded once regardless of the number of times it is imported into the python source file.
# if you want to reload the already imported module to re-execute the top-level code,
# python provides us the reload() function.
# reload(<module-name>)
# reload(platform)
