from matrix import *
from linear_algebra import *

"""
 R = Random(4,4)
id_4 = Identity(4)
res = multiply(R, id_4)

print("input")
print_matrix(R)
print("identity")
print_matrix(id_4)
print("output")
print_matrix(res)

u = [1,2,2,1]
v = [1,1,1,1]
M = outer(u,v)
print("Outer product of", u, v)
print_matrix(M)

B = Identity(3)
A = Random(2,2)
print("Kronecker product:")
K = kronecker(A,B)
print_matrix(K)
print("Matrix A:")
print_matrix(A) 

"""

A = Random(3,3) 
print_matrix(A)
print("The det is", det(A) )

