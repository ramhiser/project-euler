from numpy import array
import math

f = open('support_files/problem99.txt', 'r')
raw_data = f.read()
f.close()

# For each row in the raw_data binary tree, we construct an numpy.array
# that has each of the row's values.
# Returns a list whose elements are the binary tree's rows.
data = [row.strip().split(",") for row in raw_data.splitlines()]

values = [int(b) * math.log(int(a)) for a,b in data]
print values.index(max(values)) + 1