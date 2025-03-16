# accounts.py
# Author: Ceaman Collins
# script to return a censored version of an input account number revealing the last 4 digits

account_number = input("Please enter an 10 digit account number: ")
censored_number = ''

# adding  the Xs
for i in range(len(account_number)-4):
    censored_number += 'X'
# adding thhe last 4 digits
censored_number += account_number[-4:]

# assumptions: I have assumed that all digits except the last 4 should be covered rather than the first 6

print(censored_number)

# References used:
# https://stackoverflow.com/questions/2030053/how-to-generate-random-strings-in-python
# While not exactly what I was looking for, it gave me ideas as how to generate strings.
# I took the idea of using += to get the desired result.