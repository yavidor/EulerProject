import math
import numpy


def binominal(k, n):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


print(binominal(20, 40))


def memo(m, n):
    grid = numpy.zeros((m+1, n+1))
    for i in range(m+1):
        grid[i][0] = 1
    for j in range(n+1):
        grid[0][j] = 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
    return grid[m][n]


print(memo(20, 20))
