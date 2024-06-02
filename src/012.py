import numpy as np
# 12. How to remove from one array those items that exist in another?

# Difficulty Level: L2
# Q. From array
# a remove all items present in array b

# Input:
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

# Solution:
out = np.setdiff1d(a,b)
print(out)   # array([1,2,3,4])
