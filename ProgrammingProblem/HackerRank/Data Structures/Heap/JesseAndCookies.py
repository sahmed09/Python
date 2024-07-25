from heapq import heapify, heappush, heappop


def cookies(k, A):
    heapify(A)
    count = 0
    try:
        while A[0] < k:
            count += 1
            cookie1 = heappop(A)
            cookie2 = heappop(A)
            new_cookie = cookie1 + (2 * cookie2)
            heappush(A, new_cookie)
        return count
    except:
        return -1


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)
    print(result)
