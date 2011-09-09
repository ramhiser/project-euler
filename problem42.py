import numpy as np

# Calculates the position in the alphabet of a letter.
# We convert the letter to lowercase and then use ord()
# to find its ASCII (?) value. The lowercase letters start at 97 with 'a.'
# Example: If we call 'T' or 't', we get 20.
def letter_position(letter):
  return ord(letter.lower()) - 96

# Calculates the sum of the positions of the letters in the alphabet
# of a string.
# Example: SKY = 19 + 11 + 25 = 55
def sum_characters(string):
  return np.array([letter_position(letter) for letter in string]).sum()

f = open('support_files/problem42_words.txt', 'r')
raw_data = f.read()
f.close()

# The raw_data are stored in quotes with a comman in between, so I split them.
# The first character is botched, so I skipped it.
words = raw_data[1:].split('","')

# Calculate the first 1 million triangle numbers
nums = 10**6
triangle_numbers = set([n * (n+1) / 2 for n in range(1, nums)])

# Of the words in the downloaded file, which are triangle numbers?
# The solution consists of counting the number of triangle numbers that we find.
triangle_words = [sum_characters(word) in triangle_numbers for word in words]
print np.array(triangle_words).sum()