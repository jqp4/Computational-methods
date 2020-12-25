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
                print("{0:6.2f}".format(self.A[i][j]), end = " ")
            if b:
                print("     {0:6.2f}".format(self.B[i]))
            else:
                print()
        print()
      