"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return 0
    return 1


N = 10001
i = 2
lst = []
while 1:
    if prime(i):
        lst.append(i)
        if len(lst) == N:
            break
    i += 1
print(lst[len(lst)-1])
