def findnumofdiv(n):
    count = 0
    for i in range(1, int(n ** 0.5)):
        if n % i == 0:
            count += 2
    print()
    return count


k = 0
while findnumofdiv(int((k * (k + 1)) / 2)) < 500:
    k += 1
print(k)
