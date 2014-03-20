import numpy as np

# Determines if a string is a palindrome.
# I slightly modified the code from:
# http://www.daniweb.com/software-development/python/code/216787
def isPalindrome(phrase):
    """
    take a phrase and convert to all lowercase letters and
    ignore punctuation marks and whitespaces,
    if it matches the reverse spelling then it is a palindrome
    """
    phrase_letters = [c for c in phrase]
    #print phrase_letters  # test
    return (phrase_letters == phrase_letters[::-1])
    
# Check all the values less than a million and find those
# that are palindromes in both base-10 and base-2.
max_val = 10**6
palindromes = [i for i in range(max_val) if isPalindrome(str(i)) and isPalindrome(np.binary_repr(i))]
print np.array(palindromes).sum()