import numpy as np
# 13. How to get the positions where elements of two arrays match?
# Difficulty Level: L2

# Q. Get the positions where elements of
# a and b match

# Input:

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

# Solution:
out  = np.where( a == b)
print(out)

# #> (array([1, 3, 5, 7]),)