# es.py
# Author: Céaman Collins
# A script that takes in a file as a command line argument and
# counts the number of Es contained in the file while catching 
# certain errors.
# References used: 
# https://stackoverflow.com/questions/70797/user-input-and-command-line-arguments
# I checked this reference to understand how to get input from command line arguments.
# sys.argv was taken from this reference and with some experimentation it worked as intended.
# https://stackoverflow.com/questions/2932511/letter-count-on-a-string
# In this reference I found the .count() method for counting letters in a string.

import sys

# Start error catching

try:

    # get command line argument

    file = sys.argv[1]

    # open file as read text

    with open(file,'rt') as fp:

        # read contents

        text = fp.read()
        
        # count number of es in file

        number_of_es = text.lower().count('e')
        print(f"There are {number_of_es} es in the document.")

# catching index errors if no command line argument given

except IndexError:
    print("Please select a file as a command line argument. eg es.py 'test.txt'.")

# catching file not found errors 

except FileNotFoundError:
    print(f"Could not find file named '{file}'. Please try again.")

# catching errors when file is not a text file

except UnicodeDecodeError:
    print('Selected file is not a text file. Please try again.')