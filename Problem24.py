"""A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1,
2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""


def reverse_sublist(lst, start, end):
    lst[start:end] = lst[start:end][::-1]
    return lst


def findk(lst):
    for i in range(len(lst) - 1, 0, -1):
        if lst[i] > lst[i - 1]:
            return i - 1
    return -1


def findl(lst, k):
    for i in range(len(lst) - 1, 0, -1):
        if lst[i] > lst[k]:
            return i
    return -1


def perm(lst: list):
    listoflists = [lst]
    cop = list(reversed(sorted(lst)))
    while cop != lst:
        k = findk(lst)
        l = findl(lst, k)
        lst[k], lst[l] = lst[l], lst[k]
        reverse_sublist(lst, k + 1, len(lst))
        # print(lst)
        listoflists.append(lst[:])
    return listoflists


perms = perm([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(''.join(list(map(str, perms[999999]))))
