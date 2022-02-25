"""If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three
solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
import time
tic = time.perf_counter()
table = {}
for p in range(1001):
    table[p] = 0
    for a in range(int((p - 3) / 3)):
        for b in range(a + 1, int((p - 1 - a) / 2)):
            c = p - a - b
            if a * a + b * b == c * c:
                table[p] += 1
print(max(table, key=table.get),max(table))
toc = time.perf_counter()
print(f"{toc-tic:0.4f}")
