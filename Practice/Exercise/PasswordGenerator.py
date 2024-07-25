import string
import random

if __name__ == '__main__':
    s1 = string.ascii_lowercase
    # print(s1)
    s2 = string.ascii_uppercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)

    s = []
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    # print(s)

    # random.shuffle(s)
    # print(s)

    length = int(input("Enter the length of the password: "))
    # print("Your password is:", "".join(s[0:length]))

    # no need to use shuffle() if use sample()
    print("Your password is:", "".join(random.sample(s, length)))
