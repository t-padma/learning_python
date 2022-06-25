# MAtrix operations
#import random # to import all of random
from random import randint
from re import S  # To import only one function

def multiply(A, B):
    # assume: A is lxm matrix and B is mxn matrix
    if len(A[0]) != len(B):
        print("mismatched dimensions")
    else:
        l,m,n = len(A), len(B), len(B[0])
        emp = empty(l,n)
        for i in range(l):
            for j in range(n):
                emp[i][j] = dot(A[i], transpose(B)[j])
        return emp

def transpose(A):
    m = len(A)
    n = len(A[0])
    emp = empty(n,m)
    for i in range(n):
        for j in range(m):
            emp[i][j] = A[j][i]
    return emp

def dot(u,v):
    # u,v are row vectors
    if len(u) != len(v):
        print("mismatched dimensions")
    else:
        #emp = empty(1,len(u))[0] # empty(1,len(u)) is a "matrix"
        S = 0
        for i in range(len(u)):
            S = S + u[i]*v[i]
        return S 

def Identity(n):
    emp = empty(n,n)
    for i in range(n):
        emp[i][i] = 1
    return emp
    

def Random(m,n):
    emp = empty(m,n)
    for i in range(m):
        for j in range(n):
            emp[i][j] = randint(1,m*n)
    return emp 


def Random_binary(m,n):
    emp = empty(m,n)
    for i in range(m):
        for j in range(n):
            emp[i][j] = randint(0,1)
    return emp 


def empty(m,n):
    f = []
    for j in range(m):
        e = []
        for i in range(n):
            e.append(0)
        f.append(e)
    return f

def print_matrix(M): # input = list of lists
    for arr in M:
        print(arr)
