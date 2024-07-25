try:
    # code block where exception can occur
    a = b
except NameError:
    print("Variable 'b' is not defined\n")
except Exception as e:
    print(e)

try:
    a = 1
    b = 'str'
    c = a + b
except NameError:
    print("Variable 'b' is not defined\n")
except TypeError:
    print("datatype mismatch\n")
except Exception as e:
    print(e)

try:
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    c = a / b
    d = a * b
    e = a + b
    print(c, d, e, "\n")
except NameError:
    print("Variable 'b' is not defined\n")
except TypeError:
    print("datatype mismatch\n")
except ZeroDivisionError:
    print("second number cannot be zero\n")
except Exception as e:
    print(e)

# try else
# use the else keyword to define a block of code to be executed if no errors were raised.
# Between except and else, only one can be executed.
try:
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    c = a / b
    d = a * b
    e = a + b
except NameError:
    print("Variable 'b' is not defined\n")
except TypeError:
    print("datatype mismatch\n")
except ZeroDivisionError:
    print("second number cannot be zero\n")
except Exception as e:
    print(e)
else:
    print("c: {}, d: {}, e: {}\n".format(c, d, e))

# try else finally
# The finally block will be executed regardless if the try block raises an error or not.
# Mainly used for code cleanup.
try:
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    c = a / b
except NameError:
    print("Variable 'b' is not defined")
except TypeError:
    print("datatype mismatch")
except ZeroDivisionError:
    print("second number cannot be zero")
except Exception as e:
    print(e)
else:
    print("c: {}".format(c))
finally:
    print("The 'try except' is finished\n")
