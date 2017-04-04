"""Make a table of numbers then print the table to a CSV file. In each
row, there must be 5 positive integers and the sum of these 5 integers
must be 10. The table as a whole contains all the possible variations
of these integers, in random order, without repeating. Two different
rows may have the same integers if the integers are in a different
order. This is from <http://stackoverflow.com/questions/43201002/
random-number-list-generator-python#comment73475935_43201002>"""

from itertools import permutations
from random import shuffle

rowsize = 5
rowsum = 10
filename = 'make_table_of_5_ints_summing_to_10.csv'

# Make a table, each row of length `rowsize`, of non-decreasing positive
#   integers that sum to `rowsum`.
def maketable(sizeleft, sumleft, maxnumused, rowsofar, table):
    if sizeleft == 1:
        table.append(rowsofar + [sumleft])
    else:
        for i in range(maxnumused, sumleft // sizeleft + 1):
            maketable(sizeleft - 1, sumleft - i, i, rowsofar + [i], table)

table = []
maketable(rowsize, rowsum, 1, [], table)

# Expand the previous table, scrambling each row into all possible orders.
fulltable = [mixedrow for row in table for mixedrow in set(permutations(row))]

# Shuffle the table into random order of rows.
shuffle(fulltable)

# Write the shuffled table to a csv file without a header row.
with open(filename, 'w') as f:
    for mixedrow in fulltable:
        f.write(str(mixedrow)[1:-1] + '\n')  # remove brackets/parens from row