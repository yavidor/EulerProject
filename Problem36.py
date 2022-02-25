"""
The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""


def bothpali(d):
    if ispali(d) and ispali(bin(d)[2:]):
        return 1
    return 0


def ispali(k):
    k = str(k)
    return k == k[::-1]


count = 0
for i in range(10 ** 6):
    if ispali(i) and ispali(bin(i)[2:]):
        count += i
        print(i)
        print(bin(i)[2:])
print(count)
