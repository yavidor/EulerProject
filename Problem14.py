"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1 It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers
finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def getcollatz(n, count):
    if n != 1:
        return getcollatz(3 * n + 1, count + 1) if n % 2 == 1 else getcollatz(n / 2, count + 1)
    return count


maximum = 0
maxnum = 0
i: int
for i in range(1, 10 ** 6):
    col = getcollatz(i  , 0)
    if col > maximum:
        maximum = col
        maxnum = i
print(maxnum)
