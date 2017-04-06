"""Make a table of numbers then print the table to a CSV file. In each
row, there must be 5 positive integers and the sum of these 5 integers
must be 10. The table as a whole contains all the possible variations
of these integers, in random order, without repeating. Two different
rows may have the same integers if the integers are in a different
order. This is from <http://stackoverflow.com/questions/43201002/
random-number-list-generator-python#comment73475935_43201002>"""

from random import shuffle

rowlen = 5
rowsum = 10
filename = 'make_table_of_5_ints_summing_to_10.csv'

# Make a table, each row of length `rowlen` of positive integers that
#   sum to `rowsum`, with the rows in lexigraphical order.
def maketable(lenremains, sumremains, rowsofar, table):
    if lenremains == 1:
        table.append(rowsofar + [sumremains])
    else:
        for i in range(1, sumremains - lenremains + 2):
            maketable(lenremains - 1, sumremains - i, rowsofar + [i], table)

table = []
maketable(rowlen, rowsum, [], table)

# Shuffle the table into random order of rows.
shuffle(table)

# Write the shuffled table to a csv file without a header row.
with open(filename, 'w') as f:
    for row in table:
        f.write(str(row)[1:-1] + '\n')  # remove brackets/parens from row
