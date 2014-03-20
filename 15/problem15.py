# This problem is rather easy to calculate once the pattern is seen.
# Check out this blog post on "Counting Lattice Paths"
# http://www.robertdickau.com/lattices.html
#
# The actual answer is a centralized binomial coefficient
# More here: http://www.robertdickau.com/manhattan.html

from scipy.misc import comb
grid_size = 20
centralized_binom_coeff = comb(N=2 * grid_size, k=grid_size, exact=1)
print centralized_binom_coeff
