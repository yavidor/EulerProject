"""The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two
digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

# It simply sucks, but it works


def gcd(a, b):
    if b == 0:
        return a
    c = a % b
    return gcd(b, c)


def listtonum(lst):
    if lst[0] == 0:
        lst.remove(0)
    num = 0
    for i in range(len(lst)):
        num += lst[i] * (10 ** (len(lst) - i - 1))
    return num


def simplify_wrong(a, b):
    print(a, b)
    for dig in a:
        if dig in b and dig != 0:
            a.remove(dig)
            b.remove(dig)
    return listtonum(a), listtonum(b)


def iscancelled(n, d):
    if n % 10 == n:
        n = f'0{n}'
    if d % 10 == d:
        d = f'0{d}'
    dupn, dupd = simplify_wrong(list(map(int, str(n))), list(map(int, str(d))))
    if dupd == 0:
        return False
    return int(n) / int(d) == dupn / dupd and int(n) != dupn and int(d) != dupd


prod = 1
n, d = 1, 1
for i in range(1, 100):
    for j in range(1, i):
        if iscancelled(i, j):
            n *= i
            d *= j
print(n / gcd(n, d))
