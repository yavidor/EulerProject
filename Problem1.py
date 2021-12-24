import numpy as np

arr = np.arange(1000)
filter_arr = np.logical_or(arr % 5 == 0, arr % 3 == 0)
newarr = arr[filter_arr]
print(np.sum(newarr))
