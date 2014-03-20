import time
tic = time.time()

n = 2000000

list_of_primes = []


# Use Miller-Rabin primality test
for i in xrange( 3, n, 2 ):
    for j in list_of_primes:
        if i % j == 0:
            break
    else:
        list_of_primes.append(i)

list_of_primes.append(2)
print "Sum of the primes below 2 million: " + str(sum(list_of_primes))

toc = time.time()
print 'The result took ' + str(toc - tic) + ' seconds to compute'
