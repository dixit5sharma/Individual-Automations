import numpy as np

a = [[11,12,13],[21,22,23],[31,32,33]]
twoDArray = np.array(a)
print("ndim(1D,2D...nD) =",twoDArray.ndim)
print("Shape(tuple) =",twoDArray.shape)      # Write as 2D Matrix and y axis first element and x the second
print("Max(element) =",twoDArray.max())      # Maximum element after checking each element of 2D Matrix
print("Size =",twoDArray.size)      # Gives correct value only if x-axis = y-axis
""" Indexing - a[0][0] or a[0,0] 
Slicing also works - a[1,0:2]"""
print(twoDArray[1,0:2])     # [21 22]
print(twoDArray[1,:])       # For Full line - [21 22 23]

""" Addition in 2D Array is same as 1D array - z = x+y """
""" Scalar multiplication in 2D Array is same as 1D array - z = 2*x """
""" 2D Array multiplication in 2D Array is same as 1D array - z = x*y """

""" Matrix Multiplcation - Make sure x[columns]==y[rows] """
x = np.array([[0,1,1],[1,0,1]])
y = np.array([[1,1],[1,1],[-1,1]])
z = np.dot(x,y)
print("Matrix Multiplication of x and y is",z)
