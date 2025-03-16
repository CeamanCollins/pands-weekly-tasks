# bank.py
# Author: Ceaman Collins
# Prompt the user for two monetary values and return the sum of both values in Euro.

# Getting user input and assigning it to variables.

firstvalue = int(input("Enter amount1(in cent): "))
secondvalue = int(input("Enter amount1(in cent): "))

# Adding the two values and printing the result to 2 decimal places.

# From research I have found this method of formatting:

# print("The sum of these is €{0:.2f}".format((firstvalue + secondvalue)/100))

# or this one:

print(f"The sum of these is €{(firstvalue + secondvalue)/100:.2f}")

# References used: 
# Whirlwind Tour of Python, Built-In Types: Simple Values, Aside: Floating-point precision
# This reference was helpful in getting the right format syntax.
# https://www.w3schools.com/python/python_string_formatting.asp
# Some further research on string formatting.