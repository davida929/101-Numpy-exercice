import numpy as np
import numpy as np

# Difficulty Level: L2
# Q. Stack arrays a and b horizontally

# Input 
a = np.arange(10).reshape(2,-1)
b = np.repeat(1,10).reshape(2,-1)

# Output
 
# Method 1 
print(np.hstack([a,b]))

# Method 2 
print(np.concatenate([a, b], axis=1))

# Method 3 
print(np.c_[a, b])

