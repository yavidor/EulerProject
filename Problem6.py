def sumofsquares(n):
    return (n * (n + 1) / 2) * (n * (n + 1) / 2) - (2 * n + 1) * (n + 1) * n / 6


N = 10000000000000000000000000000000000000000000000000000000000
print(sumofsquares(N))
