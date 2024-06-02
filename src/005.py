import numpy as np
# 5. How to replace items that satisfy a condition with another value in numpy array?
# Difficulty Level: L1
# Q. Replace all odd numbers in arr with -1

# Input:
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Solution:
arr[ arr % 2 == 1] = -1
print(arr) #>  array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])