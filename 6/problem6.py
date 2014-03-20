import time
tic = time.time()

numbers = range(1,101)

print "The difference of the sum of squares and square of the sums is: " + str(sum(numbers)**2 - sum(i*i for i in numbers))

toc = time.time()
print 'The result took ' + str(toc - tic) + ' seconds to compute'
