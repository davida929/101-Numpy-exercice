import numpy as np 
# Difficulty Level: L1
# Q. Create a 3×3 numpy array of all True’s

boolean_array = np.ones((3,3), dtype='bool')
print(boolean_array)

# Alternate method 
boolean_array = np.full((3,3), True, dtype=bool)
print(boolean_array)
