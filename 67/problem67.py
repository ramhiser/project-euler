# This approach is exactly the same as in problem 18.
# The only difference here is that the triangle
# is much larger and is in a text file named 
# problem67_triangle.txt in support_files/.
from numpy import array

f = open('support_files/problem67_triangle.txt', 'r')
raw_data = f.read()
f.close()

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
