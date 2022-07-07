from matrix import empty

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

def inner(u,v):  
    return dot(u,v)

def outer(u,v):
    emp = empty(len(u), len(v))
    for i in range(len(u)):
        for j in range(len(v)):
            emp[i][j] = u[i]*v[j]
    return emp


def kronecker(A,B):
    m, n, p, q = len(A), len(A[0]), len(B), len(B[0])
    emp = empty(m*p,n*q)
    # A = [a00 a01]    B = [b00 b01]
    #     [a10 a11]        [b10 b11]
    # C = [a00*b00  a00*b01  a01*b00  a01*b01 ]  C = [c_ij]
    #        0         1         2        3
    #        00       01        10        11
    # c_ij = a_ix * b_i (j%q) where x = j//q (// gives quotient)
    # c[i][j] = A[i//p][j//q] * B[i%p][j%q]
    for i in range(m*p):
        for j in range(n*q):
            emp[i][j] = A[i//p][j//q]*B[i%p][j%q]
    return emp


def det(A):
    m, n = len(A), len(A[0])
    # a b c
    # d e f
    # g h i
    # A[0][0]*det(minor(A,0,0))* (-1)^0 + A[0][1]*det(minor(A,0,1))*(-1)^1 + A[0][2]*det(minor(A,0,2))*(-1)^2
    if m == 1 and n == 1:
        return A[0][0]

    sum = 0
    for j in range(n):
        sum = sum + A[0][j]*det(minor(A,0,j))*((-1)**j)
    return sum


def minor(A,i,j): 
    m, n = len(A), len(A[0])
    emp = empty(m-1, n - 1)
    for k in range(m-1):
        if k < i:
            emp[k] = A[k][:j] + A[k][j+1:]
        elif k >= i:
            emp[k] = A[k+1][:j] + A[k+1][j+1:]
    return emp

