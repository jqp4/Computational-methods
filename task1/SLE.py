class SLE:
    # SLE - System of linear equations
    def __init__(self, A, B):
        self.N = len(B)
        self.A = [[A[i][j] for j in range(self.N)] for i in range(self.N)]
        self.B = [B[i] for i in range(self.N)]
        #for i in range(self.N):
        #    for j in range(self.N):
        #        self.A[i][j] = A[i][j]
        #    self.B[i] = B[i]


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
        # {a-b+c-d=0, 4a-b+0-d=0,2a+b-2c+d=0,5a+b-4d=0}
        # {{-1, 4/3, -1/6, 1/6}, {-5, 26/3, -4/3, 1/3}, {-2, 7/2, -1/2, 0}, {7/4, -19/6, 7/12, -1/12}}
        # var = lambda index: f"a{index}"
        print(end="\nSLE in Wolfram language:\n{")
        for i in range(self.N):
            for j in range(self.N):
                print("+({0:.4f}*a{1})".format(self.A[i][j], j + 1), end="")
            print("={}".format(self.B[i]), end= ", " if i + 1 < self.N else "")
        print(end="}\n")
        print(end="\nA matrix in Wolfram language:\n{")
        for i in range(self.N):
            print(end="{")
            for j in range(self.N):
                print("{0:.4f}".format(self.A[i][j]), end= ", " if j + 1 < self.N else "")
            print(end= "}, " if i + 1 < self.N else "}")
        print(end="}\n")
            
      