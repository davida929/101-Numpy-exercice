import numpy as np

# Difficulty Level: L2
# Q. Replace all odd numbers in arr with -1 without changing arr


# Input:
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Input : ", arr)


# Solution :
out = arr.copy()
out[ out % 2 == 1] = -1 

print("Out : ", out)
print("arr : ", arr)

# alternative method 
out = np.where( arr % 2 == 1, -1 , arr)
print("Alt out : ", out)