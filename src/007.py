import numpy as np

# Difficulty Level: L1
# Q. Convert a 1D array to a 2D array with 2 rows

# Input  
arr = np.arange(10)
print(arr)

# Solution
out = arr.reshape((2,5))
print(out)

out = arr.reshape((2,-1))
print(out)