# The nth prime we are trying to find
import time
tic = time.time()
num_primes = 10001

list_of_primes = []
list_of_primes.append( 2 )
i = 3
while len(list_of_primes) < num_primes:
    for j in list_of_primes:
        if i % j == 0:
            break
    else:
        list_of_primes.append(i)
    i += 2
print max(list_of_primes)

toc = time.time()
print 'The result took ' + str(toc - tic) + ' seconds to compute'
