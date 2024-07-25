class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"

    def show(self):
        return f"{self.fname} {self.lname}"

    @property  # decorator
    def email(self):
        if self.fname is None or self.lname is None:
            return "Email is not set. Please set it using setter!"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter  # making this setter to set attribute from outside. without this, can't set attribute of email
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


x = Employee("Shihab", "Ahmed")
print(x.show())
print(x.email)  # for using @property before email(), we can using it like a property.. otherwise x.email()

x.fname = "Nirob"  # changing fname
print(x.email)
print()

x.email = "this.that@gmail.com"  # without setter it will raise error
print(x.fname)
print(x.lname)
print(x.email)
print()

del x.email  # if we try delete email, it will raise an error. @email.deleter property resolves this problem
print(x.email)
print()

x.email = "hello.hello@gmail.com"  # setting email again
print(x.email)
print()


class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        print("getter of x called")
        return self._x

    @x.setter
    def x(self, value):
        print("setter of x called")
        self._x = value

    @x.deleter
    def x(self):
        print("deleter of x called")
        del self._x


c = C()
c.x = 'foo'  # setter called
foo = c.x    # getter called
del c.x      # deleter called
