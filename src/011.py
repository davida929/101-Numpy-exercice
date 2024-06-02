import numpy as np

# Difficulty Level: L2
# Q. Get the common items between a and b

# Input:
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

# Solution:
out = np.unique(a[a == b]) #array([2, 4])

# Method 2
out  = np.intersect1d(a,b)
print(out)