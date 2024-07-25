from math import factorial


def solve(n, r, m):
    return (factorial(n) // factorial(r) // factorial(n - r)) % m


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nrm = input().split()

        n = int(nrm[0])

        r = int(nrm[1])

        m = int(nrm[2])

        result = solve(n, r, m)
        print(result)
