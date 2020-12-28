from SLE import SLE
from DataSet import DataSet



def relaxationMethod(sle, w, eps):
    '''
    Принимает СЛАУ, итерационный параметр и точность
    Возвращает решение системы и колличество итераций
    '''
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
            try:  # Рассчитываем норму и выходим при переполнении
                norm += delta ** 2
            except: 
                return None, -1
            xnext[i] = x[i] + delta
        norm **= (1/2)
        done = norm < eps
        iteration += 1
    return xnext, iteration



def main():
    print("\n" * 30)
    dataset = DataSet()
    sle = dataset.testsle
    sle.show(type=int)

    for eps in [0.01, 0.0001, 0.0000001]:
        print("Epsilon = {}:".format(eps))
        ws = [0.1 * i for i in range(1, 20)]    
        for w in ws:
            X, iteration = relaxationMethod(sle, w, eps)
            if X:
                print("    w = {0:.2f}, iters = {1:3d}".format(w, iteration))
            else:
                print("    Break: Too much computation, w = {0:.2f}".format(w))
                break


main() 