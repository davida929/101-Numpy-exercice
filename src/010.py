import numpy as np

# 10. How to generate custom sequences in numpy without hardcoding?

# Input :
a = np.array([1,2,3])

# Output
print(np.r_[np.repeat(a,3), np.tile(a,3)])