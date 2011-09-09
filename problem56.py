import numpy as np
import itertools

def digital_sum(n):
  digits = [i for i in str(n)]
  return np.array(map(int, digits)).sum()

max_val = 100
dig_sums = [digital_sum(a**b) for a,b in itertools.permutations(range(1, max_val), 2)]

print np.array(dig_sums).max()