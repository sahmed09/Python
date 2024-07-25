import datetime
# Python Dates
# A date in Python is not a data type of its own
# but we can import a module named datetime to work with dates as date objects.
x = datetime.datetime.now()
print(x)  # output -> year, month, day, hour, minute, second, and microsecond
print()

# Date Output
print(x)
print(x.year)
print(x.day)
print()

print(x.strftime("%A"))  # Weekday, full version
print(x.strftime("%a"))  # Weekday, short version
print(x.strftime("%w"))  # Weekday as a number 0-6, 0 is Sunday
print(x.strftime("%d"))  # Day of month 01-31
print()

print(x.strftime("%b"))  # Month name, short version
print(x.strftime("%B"))  # Month name, full version
print(x.strftime("%m"))  # Month as a number 01-12
print()

print(x.strftime("%y"))  # Year, short version, without century
print(x.strftime("%Y"))  # Year, full version
print()

print(x.strftime("%H"))  # Hour 00-23
print(x.strftime("%T"))  # Hour 00-12
print(x.strftime("%p"))  # AM/PM
print()

print(x.strftime("%M"))  # Minute 00-59
print(x.strftime("%S"))  # Second 00-59
print(x.strftime("%f"))  # Microsecond 000000-999999
print()

print(x.strftime("%z"))  # UTC offset
print(x.strftime("%Z"))  # Timezone
print()

print(x.strftime("%j"))  # Day number of year 001-366
print(x.strftime("%U"))  # Week number of year, Sunday as the first day of week, 00-53
print(x.strftime("%W"))  # Week number of year, Monday as the first day of week, 00-53
print()

print(x.strftime("%c"))  # Local version of date and time
print(x.strftime("%x"))  # Local version of date
print(x.strftime("%X"))  # Local version of time
print(x.strftime("%%"))  # A % character
print()

# Creating Date Objects
# To create a date, we can use the datetime() class (constructor) of the datetime module.
# The datetime() class requires three parameters to create a date: year, month, day.
# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone)
# but they are optional, and has a default value of 0, (None for timezone).
x = datetime.datetime(2020, 5, 13)
print(x)

# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format,to specify the format of returned string
x = datetime.datetime(2020, 8, 25)
print(x.strftime("%B"))
