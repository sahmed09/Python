import time
import datetime
import calendar

# In python, the date is not a data type
# we can work with the date objects by importing the module named with datetime, time, and calendar.

# Tick:
# A tick can be seen as the smallest unit to measure the time.
# import time
print(time.time())  # prints the number of ticks spent since 12 AM, 1st January 1970

# How to get the current time?
# import time
print(time.localtime(time.time()))  # returns a time tuple

# Getting formatted time:
# import time
print(time.asctime(time.localtime(time.time())))  # returns the formatted time

initial = time.time()
# Python sleep time:
# import time
for i in range(0, 5):
    print(i)
    time.sleep(1)  # Each element will be printed after 1 second
print("Time needed for run this loop : ", time.time() - initial)

# The datetime Module:
# The datetime module enables us to create the custom date objects
# import datetime
print(datetime.datetime.now())  # returns the current datetime object

# Creating date objects:
# import datetime
print(datetime.datetime(2018, 12, 10))  # returns the datetime object for the specified date
print(datetime.datetime(2018, 12, 10, 14, 15, 10))  # returns the datetime object for the specified time

# Comparison of two dates:
"""if datetime(datetime.now().year, datetime.now().month, datetime.now().day, 8) < datetime.now() < datetime(datetime.now().year, datetime.now().month, datetime.now().day, 16):
    print("Working hours....")
else:
    print("fun hours")"""

# The calendar module:
# import calendar
cal = calendar.month(2020, 12)
print(cal)  # #printing the calendar of December 2020

# Printing the calendar of whole year:
# import calendar
calendar.prcal(2020)  # printing the calendar of the year 2019
