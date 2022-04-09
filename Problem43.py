"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some
order, but it also has a rather interesting sub-string divisibility property.
Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""
fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]


def solution(num):
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ret = ""
    num -= 1
    for i in range(len(arr) - 1, -1, -1):
        t = int(num / fac[i]) | 0
        num %= fac[i]
        ret += str(arr[t])
        del arr[t]
    return ret


summation = 0
for i in range(3628800):
    sol = solution(i)
    if int(sol[1] + sol[2] + sol[3]) % 2 == 0 and int(sol[2] + sol[3] + sol[4]) % 3 == 0 and int(
            sol[3] + sol[4] + sol[5]) % 5 == 0 and int(sol[4] + sol[5] + sol[6]) % 7 == 0 and int(
            sol[5] + sol[6] + sol[7]) % 11 == 0 and int(sol[6] + sol[7] + sol[8]) % 13 == 0 and int(
            sol[7] + sol[8] + sol[9]) % 17 == 0:
        print(sol)
        summation += int(sol)
print(summation)
