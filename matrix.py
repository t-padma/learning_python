# MAtrix operations
#import random # to import all of random
from random import randint
# to import only one function

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
