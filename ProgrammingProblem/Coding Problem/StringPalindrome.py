s = "txt txt"
s1 = s[::-1]

if s == s1:
    print("Palindrome")
else:
    print("Not Palindrome")


############################
def palindrome(x):
    return x[::-1]


h = "ttxt"
h1 = palindrome(h)

if h == h1:
    print("Palindrome")
else:
    print("Not Palindrome")
