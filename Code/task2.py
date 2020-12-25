from SLE import SLE
from DataSet import DataSet



def main():
    print("\n" * 25)
    dataset = DataSet()
    sle = dataset.testsle
    sle.show()

    w = 1
    it = 1
    eps = 1e-4
    done = False

    x = [0 for i in range(sle.N)]
    xnext = [0 for i in range(sle.N)]
    while (not done):
        x = [xnext[i] for i in range(sle.N)]
        xnext = [0 for i in range(sle.N)]

        

        for i in range(sle.N):
            delta = sle.B[i]
            for j in range(0, i):
                delta -= sle.A[i][j] * xnext[j]
            for j in range(i - 1, sle.N):
                delta -= sle.A[i][j] * x[j]
            delta *= w / sle.A[i][i]

            xnext[i] = x[i] + delta





        v = sum([(xnext[i] - x[i]) ** 2 for i in range(sle.N)])
        done = v < eps
        it+=1
        print("iteration = {0} norm = {1:.6f}\n\txk+1 = [".format(it, v), end = "")
        for i in range(sle.N):
            print("{0:.2f}".format(xnext[i]), end = ", ")
        print(end="]\n")






main() 