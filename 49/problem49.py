import itertools

def digit_permutations(x):
    return [int(''.join(perm)) for perm in itertools.permutations(str(x), 4)]

def intersect(a, b):
    """Intersection of two lists.
    Code from: http://stackoverflow.com/questions/642763/python-intersection-of-two-lists
    """
    return list(set(a) & set(b))

max_prime = 9999

list_of_primes = [2]

# Use Miller-Rabin primality test
for i in xrange(3, max_prime, 2):
    for j in list_of_primes:
        if i % j == 0:
            break
    else:
        list_of_primes.append(i)


# We care only about the 4-digit primes.
# Thus, we filter the primes accordingly.
list_of_primes = [prime for prime in list_of_primes if prime > 1000]

# Traverse through the 4-digit primes and find the instances where the 
for prime in list_of_primes:
    primes_found = intersect(digit_permutations(prime), list_of_primes)
    primes_found.sort()
    
    for prime_i in primes_found:
        prime_pattern = [prime_i, prime_i + 3330, prime_i + 2 * 3330]
        
        # The difference in the primes must be 3330 to follow the pattern given in the problem.
        if len(intersect(prime_pattern, primes_found)) == 3:
            print prime_pattern


