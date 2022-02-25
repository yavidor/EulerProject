"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def istriple(m, n, k):
    a = k * (m * m - n * n)
    b = k * 2 * m * n
    c = (m * m + n * n) * k
    return a * a + b * b == c * c


for i in range(500):

    for j in range(i):
        for k in range(500):
            if (i * (i + j) == 500) and istriple(i, j, k):
                print(i, j)
print((20 * 20 - 25) * (2 * 20 * 5) * (20 * 20 + 25))
