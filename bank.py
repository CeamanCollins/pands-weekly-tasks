# bank
# Author: Ceaman Collins
# Prompt the user for two monetary values and return the sum of both values.

# Getting user input and assigning it to variables.
firstvalue = int(input("Enter amount1(in cent): "))
secondvalue = int(input("Enter amount1(in cent): "))
# Adding the two values and printing the result to 2 decimal places.
print("The sum of these is €{0:.2f}".format((firstvalue + secondvalue)/100))

# References used: Whirlwind Tour of Python, Built-In Types: Simple Values, Aside: Floating-point precision