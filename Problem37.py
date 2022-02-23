"""The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from
left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly, we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
import numpy


def prime(n):
    if n == 1:
        return 0
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return 0
    return 1


def primesfrom2to(n):
    sieve = numpy.ones(n // 3 + (n % 6 == 2), dtype=numpy.bool)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = False
    return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]


def istruncatable(p):
    p = str(p)
    for i in range(1, len(p)):
        if prime(int(p[i:])) == 0:
            return 0

        for i in range(1, len(p)):
            if prime(int(p[:i])) == 0:
                return 0
    return 1


print(sum([p for p in primesfrom2to(999999) if istruncatable(p)]) - 17)
