"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. 
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
"""

# Largest multiple of 3 which is < 1000 is 999, which is the last term in the sequence 3n
# The common difference is d = 3.
# Number of terms: 999 = 3 + 3(n-1) --> n = 333
# Sum formula: (333(3+999))/2 = 166,833

# Largest multiple of 5 which is < 1000 is 995, which is the last term in the sequence 5n
# The common difference is d = 5.
# Number of terms: 995 = 5 + 5(n-1) --> n = 199
# Sum formula: (199(5+995))/2 = 99,500

# Sum of both multiples of 3 and 5 below 1000L: 166,833 + 99,500 = 266,333
# Now we just need to find overlapping terms and subtract the difference
counter = 999
difference = 0
while counter > 0:
    if counter % 5 == 0:
        difference += counter
    counter -= 3

answer = 266333 - difference
print(answer)
