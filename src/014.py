import numpy as np
# How to extract all numbers between a given range from a numpy array?
# Difficulty Level: L2

# Q. Get all items between 5 and 10 from a.

# Input:
a = np.array([2, 6, 1, 9, 10, 3, 27])

# Method 1 
index = np.where((a > 5) & (a <= 10))
print(a[index])

# Method 2
print(a[(a > 5) & (a <= 10)])