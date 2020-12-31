

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
    A = lambda i: 1 / (h ** 2) - de.p(x0 + i * h) / h / 2
    B = lambda i: h ** (-2) + de.p(x0 + i * h) / h / 2
    C = lambda i: -(2 / (h ** 2)) + de.q(x0 + i * h)
    F = lambda i: de.f(x0 + i * h)
    
    a = [0, -de.g[0] / (h * de.s[0] - de.g[0])]
    b = [0, de.d[0] / (de.s[0] - de.g[0] / h)]

    for i in range(1, n):
        tmpdiv = (A(i) * a[i] + C(i))
        a.append(-B(i) / tmpdiv)
        b.append((F(i) - A(i) * b[i]) / tmpdiv)

    m = [[1, -a[n]], [1, -(h * de.s[1] + de.g[1]) / de.g[1]]]
    t = [b[n], -h * de.d[1] / de.g[1]]
    ans = np.linalg.solve(np.array(m), np.array(t))

    X = [x0 + i * h for i in range(n + 1)]
    Y = [None for i in range(n + 1)]
    Y[n] = ans[1]
    Y[n - 1] = ans[0]
    for i in range(n - 2, -1, -1):
        Y[i] = a[i + 1] * Y[i + 1] + b[i + 1]

    return X, Y





