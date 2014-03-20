max_val = 10000

# Calculates all of the factors of an integer.
# I got this code from the comments of the following blog post:
# http://www.stealthcopter.com/blog/2009/11/python-factors-of-a-number/
def proper_factors(n):
  factors = set(reduce(list.__add__, [[i, n/i] for i in range(1, int(np.sqrt(n)) + 1)
  if n % i == 0]))
  # Removes n from the set of factors because proper
  factors.remove(n)
  return factors

sum_factors = {i: sum(proper_factors(i)) for i in range(2, max_val)}
sum_factors[1] = 0

# To match the example of *amicable numbers*, the following two statements
# should be true
print sum_factors[284] == 220
print sum_factors[220] == 284

amicable_numbers = set()
for i in sum_factors.keys():
    val1 = i
    val2 = sum_factors[i]
    
    if val1 != val2 and val1 == sum_factors.get(val2, 0) and sum_factors.get(val1, 0) == val2:
        amicable_numbers.add(val1)
        amicable_numbers.add(val2)
        print "Val1: %s" % val1
        print "Val2: %s" % val2

print "Answer: %s" % str(sum(amicable_numbers))
