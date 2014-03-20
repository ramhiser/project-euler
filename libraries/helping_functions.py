# This function lists the first n primes including n, if n is prime
def list_first_n_primes( n ):
    if n < 2:
        return []
    list_of_primes = []
    list_of_primes.append( 2 )
    for i in range( 3, n + 1, 2 ):
        for j in list_of_primes:
            if i % j == 0:
                break
        else:
            list_of_primes.append(i)
    return list_of_primes
