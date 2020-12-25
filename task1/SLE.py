class SLE:
    # SLE - System of linear equations
    def __init__(self, A, B):
        self.N = len(B)
        self.A = [[A[i][j] for j in range(self.N)] for i in range(self.N)]
        self.B = [B[i] for i in range(self.N)]


    def deepcopy(self, A, B):
        for i in range(self.N):
            for j in range(self.N):
                A[i][j] = self.A[i][j]
            B[i] = self.B[i]


    def show(self, shift="", b=True):
        for i in range(self.N):
            print(end = shift)
            for j in range(self.N):
                print("{0:6.2f}x{1}".format(self.A[i][j], j + 1), end = " ")
            if b:
                print(" = {0:6.2f}".format(self.B[i]))
            else:
                print()
        print()


    def showWolframType(self):
        alph = list("qwrtuplkhgdsazvbnm")
        print(end="\nSLE in Wolfram language:\n{")
        for i in range(self.N):
            for j in range(self.N):
                aij = self.A[i][j]
                sign = ('+' if aij >= 0 else '') if i else ""
                #print("{0}{1:.1f}a{2}".format('+' if aij >= 0 else '', aij, j + 1), end="")
                print("{0}{1:.3f}{2}".format(sign, aij, alph[j]), end="")
            print("={0:.3f}".format(self.B[i]), end= ", " if i + 1 < self.N else "")
        print(end="}\n")
        print(end="\nA matrix in Wolfram language:\n{")
        for i in range(self.N):
            print(end="{")
            for j in range(self.N):
                print("{0:.3f}".format(self.A[i][j]), end= ", " if j + 1 < self.N else "")
            print(end= "}, " if i + 1 < self.N else "}")
        print(end="}\n")


    def showExcelType(self):
        alph = list("qwrtuplkhgdsazvbnm")
        '''print(end="\nSLE in Wolfram language:\n{")
        for i in range(self.N):
            for j in range(self.N):
                aij = self.A[i][j]
                sign = ('+' if aij >= 0 else '') if i else ""
                print("{0}{1:.1f}x{2}".format(sign, aij, j + 1), end="")
            print("={0:.3f}".format(self.B[i]), end= ", " if i + 1 < self.N else "")
        print(end="}\n")'''
        print(end="\nA matrix in Excel language:\n")
        for i in range(self.N):
            print(end="")
            for j in range(self.N):
                print("{0:.5f}".format(self.A[i][j]), end= ", " if j + 1 < self.N else "")
            print(end= "\n " if i + 1 < self.N else "")
        print()
            
      