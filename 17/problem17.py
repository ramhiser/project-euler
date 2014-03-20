import time
tic = time.time()

letter_sum = 0

ones_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
"sixteen", "seventeen", "eighteen", "nineteen"]
tens_words = ["filler_word_for_tens","twenty", "thirty", "forty", "fifty", "sixty", "seventy","eighty", "ninety"]

for i in xrange(1, 1000):
    third_digit = i % 10
    second_digit = i / 10 % 10
    first_digit = i / 100
    
    if second_digit < 2:
        # If the second and third digits are both zero, then no sum needs to be made
        if second_digit > 0 or third_digit > 0:
            letter_sum += len(ones_words[10*second_digit + third_digit - 1])
    else:
        letter_sum += len(tens_words[second_digit - 1])
        if third_digit > 0:
            letter_sum += len(ones_words[third_digit])
    if first_digit > 0:
        letter_sum += len(ones_words[first_digit])
        letter_sum += len("hundred")
        # The problem requires that 3 digit numbers have the British "and" construct
        # Ex. 115 => one hundred and fifteen
        if second_digit > 0 or third_digit > 0:
            letter_sum += len("and")
    print letter_sum
letter_sum += len("onethousand")
print "Letter sum: " + str(letter_sum)

toc = time.time()
print 'The result took ' + str(toc - tic) + ' seconds to compute'
