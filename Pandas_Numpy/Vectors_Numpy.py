import numpy as np

""" Vectors in Normal Python """

u = [1,0]
v = [0,1]

z=[]
for n,m in zip(u,v):
    z.append(n+m)
print(z)

""" Vectors from Numpy """

u = np.array([1,0])
v = np.array([0,1])

z = u+v
print(z)

k = u-v
print(k)

""" Scalar Multiplication in Normal Python """

y = [1,2]
z = []

for n in y:
    z.append(2*n)
print(z)

""" Scalar Multiplication with Numpy """

y = np.array([1,2])
z = 2*y
print(z)

""" Multiplication of Vectors in Normal Python """

u = [1,2]
v = [3,4]

z=[]
for n,m in zip(u,v):
    z.append(n*m)
print(z)

""" Multiplication of Vectors from Numpy """

u = np.array([1,2])
v = np.array([3,4])

z = u*v
print(z)

""" Dot Product in Numpy """

u = np.array([1,2])
v = np.array([3,4])

z = np.dot(u,v)
print(z)

""" BroadCasting or Scalar Addition to a Vector """

u = np.array([1,2,3,4,5])
z = u+1

print(z)

""" Universal Functions """

u = np.array([1,2,-3,4,5,-6])

print(u.mean())         # Mean = Sum/Count
print(u.max())          # Returns Maximum value of the array
print(np.pi)            # Numpy PI value

x = np.array([0,np.pi/2,np.pi])
y = np.sin(x)       # Applies to all the element in X

print(y)

print(np.linspace(-5,5,num=11))     # Creates a numpy array with 11 numbers equally spaces between -5 to 5

x = np.linspace(0,2*np.pi,100)
y = np.sin(x)

import matplotlib.pyplot as plt

plt.plot(x,y)
plt.show()