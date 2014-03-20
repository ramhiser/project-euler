import time
tic = time.time()

last_ten_digits = ""
digit_sum = sum( i**i for i in xrange(1,1001) )

# I copied and pasted the last 10 digits from the console window
print digit_sum

toc = time.time()
print 'The result took ' + str(toc - tic) + ' seconds to compute'
