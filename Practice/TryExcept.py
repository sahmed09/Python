# try block lets you test a block of code for errors.
# except block lets you handle the error.
# finally block lets you execute code, regardless of the result of the try- and except blocks.

# Common Exceptions:
# A list of common exceptions that can be thrown from a normal python program is given below.
"""ZeroDivisionError: Occurs when a number is divided by zero.
NameError: It occurs when a name is not found. It may be local or global.
IndentationError: If incorrect indentation is given.
IOError: It occurs when Input Output operation fails.
EOFError: It occurs when the end of the file is reached, and yet operations are being performed."""

# Exception Handling
# When an error or exception occurs, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement
try:
    print(x)
except:
    print("An exception occured")

# Many Exceptions
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

print()

# Else
# use the else keyword to define a block of code to be executed if no errors were raised.
# Between except and else, only one can be executed.
print("Use of else:")
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

try:
    print(a)
except Exception as e:
    print(e)
else:
    print("Error")

print()

# Finally
# The finally block will be executed regardless if the try block raises an error or not.
# Mainly used for code cleanup.
print("Use of finally:")
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

print()

"""try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()"""

print()

# Raise an exception:
# To throw (or raise) an exception if a condition occurs, use the raise keyword.
"""x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")"""

# You can define what kind of error to raise, and the text to print to the user.
# Raise a TypeError if x is not an integer:
"""x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")"""

"""b = 0
if b == 0:
    raise ZeroDivisionError("0 is not allowed")"""

try:
    age = 15
    if age < 18:
        raise ValueError
    else:
        print("the age is valid")
except ValueError:
    print("The age is not valid")
print()

try:
    a = 15
    b = 0
    if b is 0:
        raise ArithmeticError
    else:
        print("a/b = ", a/b)
except ArithmeticError:
    print("The value of b can't be 0")
print()


# Custom Exception:
class ErrorInCode(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


try:
    raise ErrorInCode(2000)
except ErrorInCode as ae:
    print("Received error:", ae.data)
print()

try:
    print("Try something.")
except Exception as e:
    print("Run if try fails", e)
else:
    print("Run if there is no exception.")
finally:
    print("This will be printed in every case.")
