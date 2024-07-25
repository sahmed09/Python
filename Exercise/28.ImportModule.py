import welcome as wc  # we need to create python files without using any number
import test as t1
import Datasets.test2 as t2

wc.welcome()

x = wc.add_all(10, 12)
y = t1.add_all(12, 12)
z = t2.add_all(100, 100)
print(x)
print(y)
print(z)
