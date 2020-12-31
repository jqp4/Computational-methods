from SLE import SLE
from Linalg import *
    


def gauss(sle, mainElement = True):
    N = sle.N
    A = [[sle.A[i][j] for j in range(N)] for i in range(N)]
    B = [sle.B[i] for i in range(N)]
    col = 0
    while (col < N):
        if mainElement:
            cr = getCurRow(A, col)
            swap(A, B, cr, col)
        if A[col][col] == 0:
            return None
        triangleStep(A, B, col)
        col += 1
    X = [0 for b in B]
    for i in range(N - 1, -1, -1):
        X[i] = B[i] - sum(x * a for x, a in zip(X[(i + 1):], A[i][(i + 1):]))
    return X

