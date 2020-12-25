from SLE import SLE 



def swap(A, B, r1, r2):
    if r1 != r2:
        A[r1], A[r2] = A[r2], A[r1]
        B[r1], B[r2] = B[r2], B[r1]

def triangleStep(A, B, col, BAct=True):
    div = A[col][col]
    A[col] = [a / div for a in A[col]]  #строка
    if BAct: B[col] /= div
    # сложение строки системы с другой строкой, умноженной на число
    for r in range(col + 1, len(A)):
        mul = -A[r][col]
        A[r] = [(a + k * mul) for a, k in zip(A[r], A[col])]
        if BAct: B[r] += B[col] * mul
    return div

def getCurRow(A, col):
    cr = None
    for r in range(col, len(A)):
        cr = r if cr is None or abs(A[r][col]) > abs(A[cr][col]) else cr     
    return cr

def det(inpA):
    N = len(inpA)
    A = [[inpA[i][j] for j in range(N)] for i in range(N)]
    col = 0
    determinant = 1
    while (col < N):
        cr = getCurRow(A, col)
        if cr != col:
            A[cr], A[col] = A[col], A[cr]
            determinant *= -1
        if A[col][col] == 0: 
            return 0
        determinant *= triangleStep(A, None, col, BAct=False)
        col += 1
    return determinant

def minor(A, ix, jx):
    N = len(A)
    M = [[A[i][j] for j in range(N)] for i in range(N)]
    del M[ix]
    for i in range(N - 1):
        del M[i][jx]
    return M
 
def inverse(A):
    N = len(A)
    AT = [[A[i][j] for i in range(N)] for j in range(N)]     
    result = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            tmp = minor(AT, i, j)
            result[i][j] = (-1 if (i + j) % 2 else 1) * det(tmp) / det(AT)
    #result = [[(-1 if (i + j) % 2 else 1) * det(minor(AT, i, j)) / det(AT) for j in range(N)] for i in range(N)]
    return result


norm = lambda A : max([sum([abs(c) for c in row]) for row in A])
cond = lambda A : norm(A) * norm(inverse(A))


def print_matrix(A, shift=""):
    N = len(A)
    for i in range(N):
        print("{}[".format(shift), end = "")
        for j in range(N):
            print("{0:6.2f}".format(A[i][j]), end = " ")
        print("]")
    print()       