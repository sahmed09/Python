import numpy

n, m, p = map(int, input().split())

a = numpy.array([input().strip().split() for _ in range(n)], int)
b = numpy.array([input().strip().split() for _ in range(m)], int)

print(numpy.concatenate((a, b), axis=0))

# print(numpy.concatenate((array_1, array_2), axis = 1))
