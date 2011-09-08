import numpy as np
import itertools

max_val = 28123

# Calculates all of the factors of an integer.
# I got this code from the comments of the following blog post:
# http://www.stealthcopter.com/blog/2009/11/python-factors-of-a-number/
def factors(n):
  out = set(reduce(list.__add__, [[i, n/i] for i in range(1, int(np.sqrt(n)) + 1)
  if n % i == 0]))
  return out 
# Calculates the sum of the factor of a given integer.
# Note that the above factors() function returns the number itself.
# We do not include the actual number in the sum, so we subtract it from the
# final sum.
def factor_sum(n):
  return np.array(list(factors(n))).sum() - n

# For each value between 2 and the maximum value, calculate the factors.
# Then, we calculate all of the abundant numbers in this list.
# We say a number n is abundant if the sum of the factors of n
# (including 1 but not itself) exceed n.
abundant = [i for i in range(2, max_val + 1) if i < factor_sum(i)]

sum_two_abundants = [i + j for i,j in itertools.combinations_with_replacement(abundant,2) if i + j <= max_val]

out = set(range(1, max_val + 1)) - set(sum_two_abundants)

print np.array(list(out)).sum()
