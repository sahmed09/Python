def solve(a):
    total = 1
    for i in a:
        total *= (2 ** i) + 1
    return total - 1


if __name__ == '__main__':
    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)
    print(result)
