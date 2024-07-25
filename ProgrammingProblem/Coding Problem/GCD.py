n = 30
m = 48

tot = n * m

while m != 0:
    rem = n % m
    n = m
    m = rem

gcd = n
print("GCD = ", gcd)

lcm = int(tot / gcd)
print("LCM = ", lcm)


# Highest Common Factor or Greatest Common Divisor:
def hcf(x, y):
    gcd = 0
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            gcd = i
    return gcd


a = 6
b = 9
print("GCD =", hcf(a, b))


# Least Common Multiple:
def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    return lcm


a = 6
b = 9
print("LCM =", lcm(a, b))
