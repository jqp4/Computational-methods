

class DifferentialEquation:
    def __init__(self, p, q, f, sigma, gamma, delta):
        # y''(x) + p(x) * y'(x) + q(x) * y(x) = f(x)
        self.p = p
        self.q = q
        self.f = f
        self.s = sigma
        self.g = gamma
        self.d = delta


import numpy as np


def lll(de, x0, xn, n):
    h = (xn - x0) / n
    X = [x0 + i * h for i in range(n + 1)]
    A = lambda i: h ** -2 - de.p(X[i]) / h / 2
    B = lambda i: h ** -2 + de.p(X[i]) / h / 2
    C = lambda i: -(2 / (h ** 2)) + de.q(X[i])
    F = lambda i: de.f(X[i])
    
    a = [0, -de.g[0] / (h * de.s[0] - de.g[0])]
    b = [0, de.d[0] / (de.s[0] - de.g[0] / h)]

    for i in range(1, n):
        tmpdiv = A(i) * a[i] + C(i)
        a.append(-B(i) / tmpdiv)
        b.append((F(i) - A(i) * b[i]) / tmpdiv)

    m = [[1, -a[n]], 
         [1, -(h * de.s[1] + de.g[1]) / de.g[1]]]
    t = [b[n], -h * de.d[1] / de.g[1]]
    matr_ans = np.linalg.solve(np.array(m), np.array(t))

    Y = [None for i in range(n + 1)]
    Y[n], Y[n - 1] = matr_ans[1], matr_ans[0]
    for i in range(n - 2, -1, -1):
        Y[i] = a[i + 1] * Y[i + 1] + b[i + 1]

    return X, Y





