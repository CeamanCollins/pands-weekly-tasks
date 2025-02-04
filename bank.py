#Getting user input and assigning it to variables.
x = int(input("Enter amount1(in cent): "))
y = int(input("Enter amount1(in cent): "))
#Adding the two values and printing the result to 2 decimal places.
print("The sum of these is €{0:.2f}".format((x + y)/100))