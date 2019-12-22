#importing numpy as np
import numpy as np
# to get eig() function
from numpy import linalg as rgu
#creating an array using diag function
x=np.array([[6,1,1],[4,-2,5],[2,8,7]])
y=np.diag((1,2,3))
#array of complex numbers
com=np.array([[1,-2j],[2j,5]])
#print the created arrays
print("\nmatrix x:\n",x)
print("\nmatrix y:\n",y)
print("\ncomplex matrix:\n",com)
#get the dimensions of array
print("\ndimension of matrix x:",x.ndim)
print("\ndimension of matrix y:",y.ndim)
print("\ndimension of complex matrix :",com.ndim)
#get the shape of arrays
print("\nshape of matrix x:",x.shape)
print("\nshape of matrix y:",y.shape)
print("\nshape of complex matrix x:",com.shape)
#arthematic operations using functions
print("\naddition of x,y matrices:\n",np.add(x,y))
print("\nsubtraction of x,y matrices:\n",np.subtract(x,y))
print("\nmultiplication of x,y matrices:\n",np.matmul(x,y))
print("\ndivision of x,y matrices:\n",np.divide(y,x))
#trace of matrix x
print("\ntrace of x:",np.trace(x))
#rank of matrix 
print("rank of x:",np.linalg.matrix_rank(x))
#determinant of a matrix
print("determinent of x:",np.linalg.det(x))
#inverse of matrix x
print("\nInverse of x:\n", np.linalg.inv(x))
print("\nMatrix x raised to power 3:\n",np.linalg.matrix_power(x, 3))
#calculation of eign values and vectors using eig() function
x,y = rgu.eig(x)
print("\nEigen values of matrix x are:\n",x)
print("\nEigen vectors of matrix x are:\n",y)
#calculation of eign values and vectors using eigh() function
c,d=rgu.eigh(com)
print("\nEigen values of complex matrix are:\n",c)
print("\nEigen vectors of complex matrix are:\n",d)
#Creating vectors
vector1 = 2 + 3j
vector2 = 4 + 5j
#dot product of martices x, y
product = np.dot(vector1, vector2)
print("\nDot Product :\n", product)
#dot product complex conjugate of x with y vector 
vproduct = np.vdot(vector1, vector2)
print("\nComplex conjugate Dot Product :\n ", vproduct)


