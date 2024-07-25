import datetime


class ErrorInCode(Exception):
    pass


class dobException(ErrorInCode):
    pass


year = int(input("Enter your birth year: "))
age = datetime.date.today().year - year

try:
    if 20 < age <= 30:
        print("Valid Age")
    else:
        raise dobException
except dobException:
    print("The year range is not valid")

