from SLE import SLE



class DataSet:
      def __init__(self):
            self.root = './Data/'
            # var 13
            self.sle = [self.getSLEfile(f'test{i + 1}.txt') for i in range(3)]
            inpx = float(input("Введите x для вычисления матрицы из примера 2: "))
            self.sle.append(self.getSLEcustom(inpx))
            self.len = len(self.sle)
            self.testsle = self.getSLEfile("testfile.txt")
      

      def getSLEfile(self, filename):
            with open(self.root + filename) as f:
                  read_data = f.read()
            rd1 = " ".join(read_data.split())
            rd2 = " ".join(rd1.split(sep=','))
            data = list(map(float, rd2.split()))

            n = int(len(data)**(1 / 2))
            A = [[data[i * (n + 1) + j] for j in range(n)] for i in range(n)]
            B = [data[i * (n + 1) + n] for i in range(n)]
            return SLE(A, B)


      def getSLEcustom(self, x):
            # ex 2 var 4
            M = 4
            n = 10 # 100 # для простоты проверки
            e = 2.718281828459045
            # using Euler's formula: e^ix = cosx + isinx
            cos = lambda a: (e ** (a * 1j)).imag
            bi = lambda i: n * e ** (x / i) * cos(x)
            qm = 1.001 - 2 * M * 0.001
            Aij = lambda i, j: qm**(i+j) + 0.1 * (j-i) if i!=j else (qm-1)**(i+j)
            A = [[Aij(i, j) for j in range(1, n + 1)] for i in range(1, n + 1)]
            B = [bi(i) for i in range(1, n + 1)]
            return SLE(A, B)