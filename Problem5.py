"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?
"""
import numpy

twenty = numpy.arange(1,21)
print(twenty)


def isdivisiblebyall(n):
    for pr in twenty:
        if n % pr != 0:
            return False
    return True


i = 20
while not isdivisiblebyall(i):
    i += 20
print(i)
