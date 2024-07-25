from heapq import heappush, heappop

n = int(input())

blacklist = set()
heap = []

for _ in range(n):
    operation = list(map(int, input().split()))
    if operation[0] == 1:
        heappush(heap, operation[1])
    if operation[0] == 2:
        blacklist.add(operation[1])
    if operation[0] == 3:
        while True:
            val = heappop(heap)
            if val not in blacklist:
                print(val)
                heappush(heap, val)
                break

# heap = []
# item_lookup = set()
#
#
# def push(v):
#     heappush(heap, v)
#     item_lookup.add(v)
#
#
# def discard(v):
#     item_lookup.discard(v)
#
#
# def print_min():
#     while heap[0] not in item_lookup:
#         heappop(heap)
#
#     print(heap[0])
#
#
# commands = {1: push, 2: discard, 3: print_min}
#
# n = int(input())
#
# for _ in range(n):
#     data = list(map(int, input().split()))
#     commands[data[0]](*data[1:])
