"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""


def issumofpow(n):
    # Honestly, just wanted to try make this a one liner
    return n == sum(map(powof, list(map(int, str(n)))))


def powof(n):
    return n ** 5


summation = 0
for i in range(2, 354295):
    if issumofpow(i):
        print(i)
        summation += i
print(summation)
