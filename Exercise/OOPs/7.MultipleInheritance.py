class A:
    def method_a(self):
        print('Method of class A-a')


class B(A):
    def method_a(self):
        print('Method of class B-a')

    def method_b(self):
        print('Method of class B-b')


class C(A):
    def method_a(self):
        print('Method of class C-a')


class D(B, C):
    def method_a(self):
        print('Method of class D-a')


d = D()
d.method_a()
d.method_b()
B.method_a(d)
A.method_a(d)
print()


# Call all the methods of A, B, C from A
class A:
    def method_a(self):
        print('Method of class A-a')


class B(A):
    def method_a(self):
        print('Method of class B-a')

    def method_b(self):
        print('Method of class B-b')


class C(A):
    def method_a(self):
        print('Method of class C-a')


class D(B, C):
    def method_a(self):
        print('Method of class D-a')
        A.method_a(self)
        B.method_a(self)
        C.method_a(self)


d = D()
d.method_a()
