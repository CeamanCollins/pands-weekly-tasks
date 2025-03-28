# weekday.py
# Author: Céaman Collins
# This is a script that prints out a message depending on the day
# One message for weekdays and another for weekends

# importing the datetime package

import datetime

# making a list with the days of the week that are considered the weekend

weekend = ['Saturday','Sunday']

# reference: https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
# I used this reference to find a way to check the day of the week given the date.
# reference: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
# This documentation contains a list of directives where I found %A would give me the name of the
# day of the week, which I used in my implementation.

# if the current day is in the above list it will print out the first message

if datetime.datetime.today().strftime('%A') in weekend:
    print('It is the weekend, yay!')

# otherwise it will print out the second message

else:
    print('Yes, unfortunately today is a weekday.')