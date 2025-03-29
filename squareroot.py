# squareroot.py
# Author: Céaman Collins
# Script that takes a positive floating-point number as input 
# and outputs an approximation of its square root.

# References used:
# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
# This reference contained not only a description of newton's method but also
# an example of how it can be used in python. I used a modified version
# of the example in my implementation.

def sqrt():

    # Getting N.

    user_input = float(input("Please enter a positive number: "))

    # X is any guess which can be assumed to be N or 1.

    aprox_sqrt = 1

    # Now, start a loop and keep calculating the root.

    while True:

        # root = 0.5 * (X + (N / X))

        root = 0.5 * (aprox_sqrt + (user_input / aprox_sqrt))

        # Check for the difference between the assumed X and calculated root.

        if (abs(root - aprox_sqrt) < 0.00001):

            # If the calculated root comes inside the tolerance allowed
            # then break out of the loop.

            break

        # If not yet inside tolerance then update root and continue.

        aprox_sqrt = root

    # Returning desired output values.

    return aprox_sqrt, user_input

aprox_sqrt, user_input = sqrt()
print(f"The square root of {user_input} is approx. {aprox_sqrt:.1f}.")