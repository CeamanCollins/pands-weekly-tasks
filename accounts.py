# accounts.py
# Author: Ceaman Collins
# script to return a censored version of an input account number revealing the last 4 digits

account_number = input("Please enter an 10 digit account number: ")
# https://stackoverflow.com/questions/2030053/how-to-generate-random-strings-in-python
censored_number = ''

for i in range(0,len(account_number)-4):
    censored_number += "X"
censored_number += account_number[-4:]

print(censored_number)
