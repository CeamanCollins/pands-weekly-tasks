# plottask.py
# Author: Céaman Collins
# A script that generates a plot with a histogram and a line.

# a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range 0 to 10, 

# imports

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

# initialising random number generation
# https://numpy.org/doc/stable/reference/random/generator.html
# I used this documentation page to understand what was meant by random.Generator
# in the contained documentation and to examine the examples to see how it should
# be implemented

random_numbers = np.random.default_rng().normal(loc=5,scale=2, size=1000)

# creating figure

fig, ax = plt.subplots()

# reference used:
# https://www.geeksforgeeks.org/plotting-histogram-in-python-using-matplotlib/
# This resource contained the customisation of histogram colours according to height.
# I appropriated some code from the 'Customized Histogram with Watermark' section.

# creating histogram and assigning result to variables

n, bins, patches = ax.hist(random_numbers,label='Normal Distribution')

# setting edge colour to black for each bin

for patch in patches:
    patch.set_edgecolor('black')

# getting ratios for each bin

fracs = n/n.max()

# normalising colors around the min and max ratio in fracs

norm = colors.Normalize(fracs.min(), fracs.max())

# using the ratios to give each bin a colour chosen from
# a colour map according to its relative height
# slightly adjusted to use a smaller section of the colour map

for frac, patch in zip(fracs, patches):
    colour = plt.cm.Blues(norm(frac*0.3+0.3))
    patch.set_facecolor(colour)

# generating numbers for use

x = np.arange(0,10,0.1)

# setting y variable as the cube of x

y = x ** 3

# line plot based on x and y values set above
# setting label for line, adjusting line width (lw)
# and making the line slightly transparent

ax.plot(x,y,label='$y=x^3$',lw=3,alpha=0.75)

# setting x and y bound for axis

ax.set_xbound(0,10)
ax.set_ybound(0,n.max()+50)

# setting title and axes labels

ax.set_title('plottask.py')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# adding a legend

plt.legend()

# save figure as png file

plt.savefig('plottask.png')

# show figure

plt.show()