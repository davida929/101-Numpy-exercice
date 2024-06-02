import numpy as np

# Difficulty Level: L1
# Q. Extract all odd numbers from arr

# Input:
#arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# Desired output:
#> array([1, 3, 5, 7, 9])

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
out = arr[arr % 2 == 1]
print(out)