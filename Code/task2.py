from SLE import SLE
from Gauss import gauss
from DataSet import DataSet



def main():
    dataset = DataSet()
    sle = dataset.testsle
    sle.show()

    w = 1
    eps = 1e-3
    done = False
    iteration = 0

    x = [0 for i in range(sle.N)]
    xnext = [0 for i in range(sle.N)]
    while (not done):
        norm = 0
        x = [a for a in xnext]
        xnext = [0 for i in range(sle.N)]

        for i in range(sle.N):
            delta = sle.B[i]
            for j in range(0, i - 1):
                delta -= sle.A[i][j] * xnext[j]
            for j in range(i - 1, sle.N):
                delta -= sle.A[i][j] * x[j]

            delta *= w / sle.A[i][i]
            norm += delta ** 2
            xnext[i] = x[i] + delta

        norm **= (1/2)
        done = norm < eps
        iteration += 1
        print("{0:2d}:  xk+1 = [".format(iteration), end="")
        for i in range(sle.N):
            print("{0:.2f}".format(xnext[i]), end = ", ")
        print(end="]\n")

    print("Gauss: ", gauss(sle))




main() 