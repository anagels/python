#!/usr/bin/env python

"""
    See LICENSE.txt file for copyright and license details.
"""

"""
    A bar plot with income and expense levels.
"""
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal
import sys

x_array = []
y_array = []

def load_data():
    """
        Load data
    """
    var_data = open(sys.argv[1].strip(), 'r').read()
    var_data_array = var_data.split('\n')
    i = 0
    for line in var_data_array:
        i += 1
        # skip the last 2 lines of the output
        if (len(line)>1) and (i<len(var_data_array) - 2):
            x_array.append(abs(float(line.strip().split(' ')[0].strip())))
            y_array.append(i)

load_data() # load x_array and y_array

N = 1
income = x_array[1] # ledger shows expenses first,
                    # so reverse to get income vs expenses.
expenses = x_array[0]

ind = np.arange(N)  # the x locations for the groups
width = 0.15       # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(ind+width, expenses, width, color='r')
rects2 = ax.bar(ind, income, width, color='g')

# add some
ax.set_ylabel('Value (EUR)')
title_year = ''
if len(sys.argv) > 2:
   title_year = ' - {}'.format(sys.argv[2].strip())
ax.set_title('Income vs. expenses{}'.format(title_year))
ax.set_xticks(ind+width)
ax.set_xticklabels( ('2014') )

ax.legend( (rects1[0], rects2[0]), ('Expenses', 'Income') )

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()
