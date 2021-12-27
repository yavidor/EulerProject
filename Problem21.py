"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n). If d(a) =
b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The
proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def finddivs(n):
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
    nums.append(finddivs(i))
print(nums[220])
for i in range(200, N):
    for j in range(200, i):
        if sum(nums[i]) == j and sum(nums[j]) == i and i != j:
            summation += i + j
print(summation)
