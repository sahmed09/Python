# The diamond problem occurs when two classes have a common ancestor,
# and another class has both those classes as base classes.
# Python doesn't have this problem because of the method resolution order.
# when you inherit from multiple classes, if their method names conflict, the first one named takes precedence.


class A:
    def met(self):
        print("Class A")


class B(A):
    def met(self):
        print("Class B")


class C(A):
    def met(self):
        print("Class C")


class D(C, B):
    pass


d = D()
d.met()


class D(B, C):
    pass


d = D()
d.met()


class D(B, C):
    def met(self):
        print("Class D")


d = D()
d.met()
