"""import numpy

for i in numpy.arange(0, 2.2, 0.2):
    if i == 0 or i == 1 or i == 2:
        print("I=%.0f J=%.0f" % (i, i+1))
        print("I=%.0f J=%.0f" % (i, i+2))
        print("I=%.0f J=%.0f" % (i, i+3))
    else:
        print("I=%.1f J=%.1f" % (i, i + 1))
        print("I=%.1f J=%.1f" % (i, i + 2))
        print("I=%.1f J=%.1f" % (i, i + 3))"""

i = 0
j = 1
value = 0
temp = 0
temp2 = 0
while i <= 2:
    if temp2 == 0:
        print("I=%.0f J=%.0f" % (i, j))
    else:
        print("I=%.1f J=%.1f" % (i, j))

    temp += 1
    if temp == 3:
        i += 0.2
        value += 0.2
        j = value
        temp = 0
        temp2 += 1

    if temp2 == 5:
        temp2 = 0
    j += 1
