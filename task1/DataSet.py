from SLE import SLE



class DataSet:
      # 13 вариант
      def __init__(self):
            self.sle = []
            A1 = [[ 3, -2,  2, -2],
                  [ 2, -1,  2,  0],
                  [ 2,  1,  4,  8],
                  [ 1,  3, -6,  2]]
            B1 =  [ 8,  4, -1,  3]
            self.sle.append(SLE(A1, B1))
            A2 = [[ 2,  3,  1,  2],
                  [ 4,  3,  1,  1],
                  [ 1, -7, -1, -2],
                  [ 2,  5,  1,  1]]
            B2 =  [ 4,  5,  7,  1]
            self.sle.append(SLE(A2, B2))
            A3 = [[ 1, -1,  1, -1],
                  [ 4, -1,  0, -1],
                  [ 2,  1, -2,  1],
                  [ 5,  1,  0, -4]]
            B3 =  [ 0,  0,  0,  0]
            self.sle.append(SLE(A3, B3))
            Af = [[],
                  [],
                  [],
                  []]
            Bf =  []







            #self.sle.append(SLE(Af, Bf))
            self.len = len(self.sle)

            myA = [[1.0, -2.0, 3.0, -4.0],
                        [3.0, 3.0, -5.0, -1.0],
                        [3.0, 0.0, 3.0, -10.0],
                        [-2.0, 1.0, 2.0, -3.0]]
            myB = [2.0, -3.0, 8.0, 5.0]
            self.sle0 = SLE(myA, myB)
        

