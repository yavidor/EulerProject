def ispali(k):
    return k == k[::-1]


largest = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        if ispali(str(i * j)) and (i * j) > largest:
            largest = i * j
print(largest)
