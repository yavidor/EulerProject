"""We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for
example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1
through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum
"""


def containsall(n, k, r):
    lst = list(str(n)) + list(str(k)) + list(str(r))
    checkto = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return sorted(lst) == checkto


def ispandi(n):
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if containsall(n, i, int(n / i)):
                return n
    return 0


sett = set()
for i in range(10000):
    sett.add(ispandi(i))
print(sum(sett))
