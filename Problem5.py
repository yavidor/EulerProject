import numpy

twenty = numpy.arange(1,21)
print(twenty)


def isdivisiblebyall(n):
    for pr in twenty:
        if n % pr != 0:
            return False
    return True


i = 20
while (isdivisiblebyall(i) != True):
    i += 20
print(i)
