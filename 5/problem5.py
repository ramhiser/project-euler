import time
tic = time.time()

isDone = 0
# I picked 2520 because the problem gives that this is the smallest number that is divisible by 1 to 10
i = 2520
while not isDone:
    i += 20
    # Is i divisible by 1 through 20? (inclusively)
    # I was able to prune 1 through 10 because each are prime factors of some number
    # between 1 and 20 (inclusively)
    for j in xrange(11,21):
        if i % j != 0:
            break
    else:
        isDone = 1
print i

toc = time.time()
print 'The result took ' + str(toc - tic) + ' seconds to compute'
