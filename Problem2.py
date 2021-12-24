def fib(n):
    a, b = 0, 1
    c = 0
    while a < n:
        if (a % 2 == 0):
            c += a
        a, b = b, a + b
    return c


print(fib(4000000))
