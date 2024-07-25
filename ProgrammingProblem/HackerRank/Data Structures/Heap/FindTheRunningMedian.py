import bisect


def runningMedian(a):
    temp = []
    result = []

    for i in a:
        bisect.insort(temp, i)
        mid = len(temp) // 2
        if len(temp) % 2 == 0:
            result.append(round((temp[mid - 1] + temp[mid]) / 2, 1))
        else:
            result.append("%.1f" % temp[mid])
    return result


if __name__ == '__main__':
    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = runningMedian(a)
    print(*result, sep="\n")
