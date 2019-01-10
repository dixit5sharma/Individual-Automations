import numpy as np

a = np.array([0,1,2,3,4])
print(a)
print(type(a))
print(a.dtype)      # 32 bit integer
print(a.size)
print(a.ndim)       # Array dimensions
print(a.shape)      # tuple with size in each dimension

a[0] = 100      # Assigning value from indexing
print(a)

print(a[1:4])       # Slicing - Print from index 1 to 3

a[1:3] = 200,300        # Slicing Assignmnent
print(a)
