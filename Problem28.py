"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
import numpy as np
N = 5
arr = np.zeros((N, N), dtype=int)
x, y = len(arr) - 1, 0
direction = ["left", "down", "right", "up"]
dircount = 0
n = arr.size
while n > 0:
    arr[y][x] = n
    if dircount % 4 == 0:
        if arr[y][x - 1] != 0 or x == 0:
            y += 1
            dircount += 1
        else:
            x -= 1
    elif dircount % 4 == 1:
        if y == len(arr) - 1 or arr[y + 1][x] != 0:
            x += 1
            dircount += 1
        else:
            y += 1
    elif dircount % 4 == 2:
        if  x == len(arr)-1 or arr[y][x + 1] != 0:
            y -= 1
            dircount += 1
        else:
            x += 1
    else:
        if arr[y-1][x] != 0 or y == 0:
            x -= 1
            dircount += 1
        else:
            y -= 1
    n -= 1
print(arr)
print(arr.diagonal())
print(np.fliplr(arr).diagonal())
print(sum(arr.diagonal())+sum(np.fliplr(arr).diagonal()))