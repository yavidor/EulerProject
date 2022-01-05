"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
import numpy as np


def prime(n):
    if n in allprimes:
        return True
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def listtonum(lst):
    times = 0
    while lst[0] == 0:
        times += 1
        lst.pop(0)
    num = 0
    for i in range(len(lst)):
        num += lst[i] * (10 ** (len(lst) - i - 1))
    return num * (10 ** times)


def shift(n: int):
    """
    shifts a number to the left
    :param n: the number
    :return: the shifted number
    """
    n = list(map(int, str(n)))
    n.insert(0, n.pop())
    return listtonum(n)


def primesfrom2to(n):
    # No idea how it works, no idea what it means
    sieve = np.ones(n // 3 + (n % 6 == 2), dtype=np.bool)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = False
    return np.r_[2, 3, ((3 * np.nonzero(sieve)[0][1:] + 1) | 1)]


def checkallshifts(n):
    for i in range(len(str(n)) - 1):
        n = shift(n)
        if not prime(n):
            return 0
    return 1


count = 0
allprimes = primesfrom2to(10 ** 2)
for primes in allprimes:
    count += checkallshifts(primes)
print(count)
