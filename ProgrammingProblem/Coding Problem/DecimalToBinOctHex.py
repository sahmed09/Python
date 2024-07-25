dec = int(input("Enter a decimal number : "))

print(bin(dec), "in binary")
print(oct(dec), "in octal")
print(hex(dec), "in hexadecimal")

n = int(input())
w = len("{0:b}".format(n))
for i in range(1, n+1):
    print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=w))
