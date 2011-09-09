import numpy as np
import itertools

nums = 1000000
# Joins the first digits together.
# Example: 1234567891011121314151617181920...
digits = ''.join([str(i) for i in range(1,nums)])
solution = int(digits[1 - 1]) * int(digits[10 - 1])
solution *= int(digits[10**2 - 1]) * int(digits[10**3 - 1])
solution *= int(digits[10**4 - 1]) * int(digits[10**5 - 1]) * int(digits[10**6 - 1])

print solution
