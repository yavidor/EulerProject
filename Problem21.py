def findnumofdiv(n):
    divs = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if i * i != n:
                divs.append(n / i)
    return divs


nums = []
summation = 0
N = 10000
for i in range(N):
    nums.append(findnumofdiv(i))
print(nums[220])
for i in range(200, N):
    for j in range(200, i):
        if sum(nums[i]) == j and sum(nums[j]) == i and i != j:
            summation += i + j
print(summation)
