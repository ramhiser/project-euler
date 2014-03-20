digit_sum = 0

for letter in str(2**1000):
    digit_sum += int(letter)
    
print digit_sum
