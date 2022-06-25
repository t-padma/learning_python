from matrix import *

R = Random(4,4)
id_4 = Identity(4)
res = multiply(R, id_4)

print("input")
print_matrix(R)
print("identity")
print_matrix(id_4)
print("output")
print_matrix(res)