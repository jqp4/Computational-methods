from SLE import SLE
from DataSet import DataSet
from linalg import print_matrix, vecnorm



def main():
    print("\n" * 25)
    dataset = DataSet()
    sle = dataset.testsle
    sle.show()

    w = 1
    it = 1
    eps = 0.001
    done = False

    x = [0 for i in range(sle.N)]
    xnext = [0 for i in range(sle.N)]
    while (not done):
        x = [xnext[i] for i in range(sle.N)]
        xnext = [0 for i in range(sle.N)]
        for i in range(sle.N):
            mul = sle.B[i]
            for j in range(0, i):
                mul -= sle.A[i][j] * xnext[j]
            for j in range(i - 1, sle.N):
                mul -= sle.A[i][j] * x[j]
            xnext[i] = x[i] + w * mul / sle.A[i][i]





        v = sum([(xnext[i] - x[i]) ** 2 for i in range(sle.N)])
        done = v < eps
        it+=1
        print("iter = {} ||xk+1 - x|| = {}\n    xk+1 = [".format(it, 
            vecnorm([xnext[i] - x[i] for i in range(sle.N)])), end = "")
        for i in range(sle.N):
            print("{0:.2f}".format(xnext[i]), end = ", ")
        print(end="]\n")






main() 