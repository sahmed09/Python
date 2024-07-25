try:
    yearAge = int(input("What is your age/year of birth? "))
    isAge = False
    isYear = False

    if len(str(yearAge)) == 4:
        isYear = True
    elif len(str(yearAge)) == 2:
        isAge = True
    else:
        print("No a valid input.")
        exit()

    if yearAge < 1920 and isYear:
        print("It's a lot surprising that you are still alive!")
        exit()

    if yearAge > 2020 and isYear:
        print("You are not yet born! LOL!!!")
        exit()

    if isAge:
        yearAge = 2020-yearAge

    print(f"You will be 100 years old in {yearAge + 100}\n")

    interestedYear = int(input("Enter the year you want to know your age in: "))

    if interestedYear < yearAge:
        print(f"You born in the year of {yearAge}. So you can't know your age before your birth.")
    else:
        print(f"You will be {interestedYear - yearAge} years old in {interestedYear}.")

except Exception as e:
    print(e)

# except ValueError:
#     print("Wrong input")
