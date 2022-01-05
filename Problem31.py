"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
import numpy as np


def solution(target):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    table = np.zeros((target + 1, len(coins)))
    for i in range(target + 1):
        table[i][0] = 1
    print(table)
    for i in range(target + 1):
        for j in range(1, len(coins)):
            table[i][j] = table[i][j - 1];
            if coins[j] <= i:
                table[i][j] += table[i - coins[j]][j]
    print(table)
    return table[i - 1][j - 1];


def solution1(target):
    coins = [1, 2, 5, 10, 20, 50, 100, 200];
    table = np.zeros(target + 1);
    table[0] = 1;
    for i in range(len(coins)):
        for j in range(coins[i], target + 1):
            table[j] += table[j - coins[i]]
    return table[target]


print(solution1(200))
