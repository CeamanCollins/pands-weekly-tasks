# plottask.py
# Author: Céaman Collins
# A script that generates a plot with a histogram and a line.

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

# https://www.geeksforgeeks.org/plotting-histogram-in-python-using-matplotlib/
# This resource contained the customisation of histogram colours according to height.
# I appropriated some code from the 'Customized Histogram with Watermark' section.

# creating histogram and assigning result to variables

n, bins, patches = ax.hist(random_numbers,label='Normal Distribution', bins=9)

# setting edge colour to black for each bin

for patch in patches:
    patch.set_edgecolor('tab:blue')

# getting fractions of the maximum for each bin

fracs = n/n.max()

# normalising the fractions and mapping them 
# linearly to values from 0 to 1

norm = colors.Normalize(fracs.min(), fracs.max())

# using the normalisation to give each bin a colour chosen from
# a colour map according to its relative height
# slightly adjusted to use a smaller section of the colour map
# for paler colours

for frac, patch in zip(fracs, patches):
    colour = plt.cm.Blues(norm(frac)*0.4+0.3)
    patch.set_facecolor(colour)

# generating numbers for use

x = np.arange(0,10,0.1)

# setting y variable as the cube of x

y = x ** 3

# line plot based on x and y values set above
# setting label for line, adjusting line width (lw)
# and making the line slightly transparent

ax.plot(x,y,label='$y=x^3$',lw=3,alpha=0.75)

# setting x bound for axis taking n from histogram plot

ax.set_xbound(0,10)
ax.set_ybound(0,n.max()+50)

# setting title and axes labels

ax.set_title('plottask.py')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_xticks([1,3,5,7,9])

# adding a legend

plt.legend()

# save figure as png file

plt.savefig('./pands-weekly-tasks/plottask.png')

# show figure

plt.show()