from numpy import array
raw_data = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

# For an individual row in the binary tree, we return the maximum value
# of each pair.
# As an example, consider the 4th line from above. The max_pairs
# of 18 35 87 10 would be 35 87 87.
def max_pairs(li):
  return(array([max(li[i], li[i+1]) for i in (range(len(li) - 1))]))

# For each row in the raw_data binary tree, we construct an numpy.array
# that has each of the row's values.
# Returns a list whose elements are the binary tree's rows.
data = [array(map(int, row.strip().split())) for row in raw_data.splitlines()]
data.reverse()

# This is the core algorithm to solve the puzzle.
# Start at the bottom of the tree, and find the max pairs.
# Then add these to the row above it. This collapses the
# original tree into a tree with one fewer rows.
# Also, this approach allows us to avoid brute-forcing the
# maximum sum.
tree_sum = max_pairs(data[0]) + data[1] 
for i in range(1, len(data) - 1):
  tree_sum = max_pairs(tree_sum) + data[i+1] 

print(tree_sum)
