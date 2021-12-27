"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def ispali(k):
    return k == k[::-1]


largest = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        if ispali(str(i * j)) and (i * j) > largest:
            largest = i * j
print(largest)
