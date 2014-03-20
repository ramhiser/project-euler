from math import sqrt
import time
tic = time.time()

num_factors = 0
i = 200000000
while num_factors <= 500:
    num_factors = 0
    triangle_number = sum( n for n in range( 1, i + 1) )
    for j in range( 2, int( sqrt( triangle_number + 1 ) ) + 1 ):
        if triangle_number % j == 0:
            num_factors += 1
    # Adding in the factors 1 and the number itself
    num_factors += 2
#    if num_factors > 500:
#        break            
    i += 1

print i-1

toc = time.time()
print 'The result took ' + str(toc - tic) + ' seconds to compute'
