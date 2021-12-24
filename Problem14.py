import numpy as np


def getcollatz(n, count):
    if n != 1:
        return getcollatz(3 * n + 1, count + 1) if n % 2 == 1 else getcollatz(n / 2, count + 1)
    return count


maximum = 0
maxnum = 0
i: int
for i in range(1, 10**6):
    col = getcollatz(i,0)
    if col > maximum:
        maximum = col
        maxnum = i
print(maxnum)
