import time
tic = time.time()

max_starting_number = 1
max_chain_length = 1
for i in xrange(1, 1000001):
    current_number = i
    chain_length = 1    

    while current_number != 1:
        if current_number % 2 == 0:
            current_number /= 2
        else:
            current_number = 3 * current_number + 1
        chain_length += 1
        
    if chain_length > max_chain_length:
        max_chain_length = chain_length
        max_starting_number = i

print max_starting_number

toc = time.time()
print 'The result took ' + str(toc - tic) + ' seconds to compute'
