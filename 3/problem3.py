from math import sqrt

number_to_factor = 600851475143
prime_factors = []

for i in range( 3, int( sqrt( number_to_factor ) ), 2 ):
    if i > number_to_factor:
        break
    if number_to_factor % i == 0:
        prime_factors.append(i)
    while number_to_factor % i == 0:
        number_to_factor /= i
        
print max(prime_factors)
