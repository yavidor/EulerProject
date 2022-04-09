"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For
example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
"""
import time

global lst
lst = list()
tic = time.perf_counter()


def prime(n):
    if n == 1:
        return 0
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return 0
    return 1


def permute(a, left, right):
    if left == right:
        string = int(''.join(a))
        if prime(string):
            lst.append(string)
    else:
        for i in range(left, right + 1):
            a[left], a[i] = a[i], a[left]
            permute(a, left + 1, right)
            a[left], a[i] = a[i], a[left]


permute(list("1234567"), 0, 6)
print(lst)
print(max(lst))
toc = time.perf_counter()
print(toc-tic)
