"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
N = 28123


def finddivs(n):
    divs = [1]
    lim = int(n ** 0.5) + 1
    for i in range(2, lim):
        if n % i == 0:
            divs.append(i)
            if i * i != n:
                divs.append(int(n / i))
    return sum(divs) > n


def issumoftwo(n, ums):
    sumset = set()
    for first in ums:
        for second in ums:
            if (first + second) > n:
                break
            else:
                sumset.add(first + second)
    return sumset


num = []
for i in range(1, N):
    if finddivs(i):
        num.append(i)
sums = issumoftwo(N, num)
total = 0
for i in range(N + 1):
    if i not in sums:
        total += i
print(total)
