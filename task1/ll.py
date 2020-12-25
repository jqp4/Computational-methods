from SLE import SLE
from Gauss import gauss
from DataSet import DataSet
from linalg import *
import numpy as np


'''def pm(A):
    N = len(A)
    for i in range(N):
        for j in range(N):
            print(A[i][j], end = " ")
        print()
    print()      


a = np.matrix([[1, 1, 1],
               [2, 2, 1],
               [3, 3, 0]])
#pm(a)
print(np.linalg.cond(a))


A = [[6, 4, 3],
     [2, 1, 3],
     [7, 5, 2]]
x =  np.matrix(A)'''




matrix = [
    [1, -123, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [[1, 1, 1],
               [2, 2, 1],
               [3, 3, 0]]
 
m = 3
n = 3
 
# L1
a = []
for i in range(m):
    row_abs = [abs(matrix[i][j]) for j in range(n)]
    a.append(sum(row_abs))

print(f'my L1 - {max(a)}')
 
# L∞
a = []
for j in range(n):
    col_abs = [abs(matrix[i][j]) for i in range(m)]
    a.append(sum(col_abs))
print(f'my L inf - {max(a)}')


d = np.matrix(matrix)
print("np L1 - ", np.linalg.norm(d, 1))
print("np L2 - ", np.linalg.norm(d, 2))




print("nk - ", norm)
MA = norm