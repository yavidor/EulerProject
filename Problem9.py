def istriple(m, n):
    a = m * m - n * n
    b = 2 * m * n
    c = m * m + n * n
    return a * a + b * b == c * c


for i in range(500):
    for j in range(i):
        if (i * (i + j) == 500) and istriple(i, j):
            print(i, j)
print((20*20-25)*(2*20*5)*(20*20+25))