"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""
import numpy as np

summation = 0

for i in range(3, np.math.factorial(9) * 6):
    if sum(list(map(np.math.factorial, map(int, str(i))))) == i:
        print(i)
        summation += i
print(summation)
