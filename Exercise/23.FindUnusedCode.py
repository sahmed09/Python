import os
import numpy as np
import pandas as pd

# pip install vulture
"""To find out dead code, go to terminal and write 
cd .\Exercise\
vulture filename.py  (vulture 23.FindUnusedCode.py)"""


class Greet:
    def greet(self):
        print('Hello')


def hello():
    var = 123
    var2 = 123+34
    var3 = 10
    message = 'Hello World'
    greeter = Greet()
    greet_func = getattr(greeter, 'greet')
    greet_func()


if __name__ == '__main__':
    hello()
