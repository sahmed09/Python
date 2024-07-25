def quartile(data):
    size = len(data)
    if size % 2 == 0:
        return (data[size // 2 - 1] + data[size // 2]) / 2
    else:
        return data[size // 2]


n = int(input())
data = list(map(int, input().split()))
freq = list(map(int, input().split()))

s = []
for i in range(n):
    s += [data[i]] * freq[i]
N = sum(freq)
s.sort()

if N % 2 != 0:
    q1 = quartile(s[:N // 2])
    q3 = quartile(s[N // 2 + 1:])
else:
    q1 = quartile(s[:N // 2])
    q3 = quartile(s[N // 2:])

print(round(float(q3 - q1), 1))

# # using statistics
# import statistics as st
#
# n = int(input())
# data = list(map(int, input().split()))
# freq = list(map(int, input().split()))
#
# s = []
# for i in range(n):
#     s += [data[i]] * freq[i]
# N = sum(freq)
# s.sort()
#
# if n % 2 != 0:
#     q1 = st.median(s[:N // 2])
#     q3 = st.median(s[N // 2 + 1:])
# else:
#     q1 = st.median(s[:N // 2])
#     q3 = st.median(s[N // 2:])
#
# ir = round(float(q3 - q1), 1)
# print(ir)
