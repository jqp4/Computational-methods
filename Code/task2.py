from SLE import SLE
from DataSet import DataSet



def relaxationMethod(sle, w, eps):
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
            try:
                norm += delta ** 2
            except: 
                return None, -1
            xnext[i] = x[i] + delta
        norm **= (1/2)
        done = norm < eps
        iteration += 1
    return (xnext, iteration)




def main():
    print("\n" * 30)
    dataset = DataSet()
    sle = dataset.testsle
    sle.show()

    for eps in [0.01, 0.0001, 0.0000001]:
        print("[eps = {}]".format(eps))
        w = 0
        dw = 0.1
        while w < 2 - dw :  
            w += dw      
            X, iteration = relaxationMethod(sle, w, eps)
            if X:
                print("    w = {0:.2f}, iters = {1:3d}".format(w, iteration))
            else:
                print("    Break: Too much computation, w = {0:.2f}".format(w))
                break


main() 




'''3 -1 1 3
1 1 1 5
4 -1 4 5'''