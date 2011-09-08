import numpy as np

# Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
def triangle(n):
    return n * (n + 1) / 2

# Pentagonal	 	Pn=n(3n1)/2	 	1, 5, 12, 22, 35, ... 
def pentagonal(n):
  return n * (3*n - 1) / 2

# Hexagonal	 	Hn=n(2n1)	 	1, 6, 15, 28, 45, ...  
def hexagonal(n):
  return n * (2*n - 1)
  
# The purpose of this problem is to find the largest number after
# 40755 = T_285 = P_165 = H_143 that is in the triangle, pentagonal,
# and hexagonal sequences.
# To do this, I'm simply compling a set of B values from each sequence
# and then displaying the intersection of the lists.
B = 100000
tri_set = set([triangle(i) for i in range(1, B)])
pen_set = set([pentagonal(i) for i in range(1, B)])
hex_set = set([hexagonal(i) for i in range(1, B)])

print tri_set & pen_set & hex_set
