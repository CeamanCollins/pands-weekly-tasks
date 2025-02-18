# collatz.py
# Author: Céaman Collins
# This script takes in a value then divides by two if 
# the value is even and multiplies by 3 and adds 1 if
# the value is odd finishing then if the value is exactly 1.
# It then prints all the values covered by the script.

# getting start value and creating empty list
current_value = int(input("Please enter a positive integer: "))
values_list = []

# while loop for iteration
while current_value != 1:
    #saving iterated values
    values_list.append(current_value)
    # testing for even numbers
    if not current_value % 2:
        current_value = int(current_value/2)
    # if not even then odd
    else:
        current_value = current_value * 3 + 1

# if the current value is 1 the while loop is not completed
# so adding manually
values_list.append(1)

# Reference: https://stackoverflow.com/questions/15769246/pythonic-way-to-print-list-items
# Reference: A Whirlwind Tour of Python by Jake VanderPlas, Iterators: Iterators as function arguments
print(*values_list)