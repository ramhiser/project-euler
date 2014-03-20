import time
tic = time.time()

sequence = []

for a in xrange(2,101):
    for b in xrange(2,101):
        sequence.append(a**b)

print len(set(sequence))

toc = time.time()
print 'The result took ' + str(toc - tic) + ' seconds to compute'
