from SLE import SLE
from math 


class DataSet:
      # var 13
      def __init__(self):
            self.sle = []
            A1 = [[ 3, -2,  2, -2],
                  [ 2, -1,  2,  0],
                  [ 2,  1,  4,  8],
                  [ 1,  3, -6,  2]]
            B1 = [ 8,  4, -1,  3]
            self.sle.append(SLE(A1, B1))
            A2 = [[ 2,  3,  1,  2],
                  [ 4,  3,  1,  1],
                  [ 1, -7, -1, -2],
                  [ 2,  5,  1,  1]]
            B2 = [ 4,  5,  7,  1]
            self.sle.append(SLE(A2, B2))
            A3 = [[ 1, -1,  1, -1],
                  [ 4, -1,  0, -1],
                  [ 2,  1, -2,  1],
                  [ 5,  1,  0, -4]]
            B3 = [ 0,  0,  0,  0]
            self.sle.append(SLE(A3, B3))

            # ex 2 var 4
            M = 4
            n = 100
            e = 2.718281828459045
            # using Euler's formula: e^ix = cosx + isinx
            cos = lambda x: (e**(X * 1j)).imag
            bi = lambda x, i: n * e**(x / i) * cos(x)
            qm = 1.001 - 2 * M * 0.001
            Aij = lambda i, j: qm**(i+j) + 0.1 * (j-i) if i!=j else (qm-1)**(i+j)
            Af = [[Aij(i, j) for j in range(n)] for i in range(n)]
            Bf = [bi(i) for i in range(n)]

            self.sle.append(SLE(Af, Bf))
            self.len = len(self.sle)

            myA = [[1.0, -2.0, 3.0, -4.0],
                   [3.0, 3.0, -5.0, -1.0],
                   [3.0, 0.0, 3.0, -10.0],
                   [-2.0, 1.0, 2.0, -3.0]]
            myB = [2.0, -3.0, 8.0, 5.0]
            self.sle0 = SLE(myA, myB)
        

