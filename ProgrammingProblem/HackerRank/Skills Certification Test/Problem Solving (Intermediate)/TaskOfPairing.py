#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'authEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY events as parameter.
#

def authEvents(events):
    s = ""
    result = []
    total1 = 0
    total2 = 0
    for event in events:
        if event[0] == "setPassword":
            setpass = event[1]
            count = len(setpass)-1
            for i in setpass:
                total1 += (ord(i) * 131 ** count)
                count -= 1
            total1 = total1 % (10 ** 9 + 7)
            print(total1)
        else:
            password = event[1]
            if total1 == int(password):
                result.append(1)
            # else:
            #     subs = int(password) - total1
            #     print(subs)
            #     char = chr(subs)
            #     if len(char) == 1:
            #         result.append(1)
            #     else:
            #         result.append(0)
                result.append(0)
    return result


if __name__ == '__main__':
    events_rows = int(input().strip())
    events_columns = int(input().strip())

    events = []

    for _ in range(events_rows):
        events.append(input().rstrip().split())

    result = authEvents(events)
    print(result)
