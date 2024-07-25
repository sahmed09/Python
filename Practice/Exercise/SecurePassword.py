secure = (('s', '$'), ('and', '&'), ('a', '@'), ('i', '1'), ('o', '0'))


def secure_password(password):
    for a, b in secure:
        password = password.replace(a, b)
    return password


if __name__ == '__main__':
    password = input("Enter your password: ").lower()
    password = secure_password(password)
    print(f"Your password is {password}")

