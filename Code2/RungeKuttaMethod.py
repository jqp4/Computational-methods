

def rk2(f, x0, y0, l, n):
    # Метод Рунге-Кутта 2 порядка точности
    h = l / n
    X = [x0 + i * h for i in range(n + 1)] # делим отрезок [x0, x0 + l] на n частей
    Y = [y0] # y(x0) = y0
    for i in range(n):
        xi = X[i]
        yi = Y[i]
        k1 = f(xi, yi)
        k2 = f(xi + h, yi + k1 * h)
        # По рекурентной формуле вычисляем следующий y:
        Y.append(yi + h * (k1 + k2) / 2)
    return X, Y
    
    
def rk4(f, x0, y0, l, n):
    # Метод Рунге-Кутта 4 порядка точности
    h = l / n
    X = [x0 + i * h for i in range(n + 1)] # делим отрезок [x0, x0 + l] на n частей
    Y = [y0] # y(x0) = y0
    for i in range(n):
        xi = X[i]
        yi = Y[i]
        k1 = f(xi, yi)
        k2 = f(xi + h / 2, yi + k1 * h / 2)
        k3 = f(xi + h / 2, yi + k2 * h / 2)
        k4 = f(xi + h, yi + k3 * h)
        # По рекурентной формуле вычисляем следующий y:
        Y.append(yi + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6)
    return X, Y






def linearComb(arrays, consts=[]):
    n = len(arrays[0])
    ans = [0 for i in range(n)]
    if len(consts) == 0:
        consts = [1 for i in range(n)]
    for a, c in zip(arrays, consts):
        if a == 1:
            a = [1 for i in range(n)]
        for i in range(n):
            ans[i] += a[i] * c
    return ans



def rk4_sys(f, x0, y0, l, n):
    # Метод Рунге-Кутта 4 порядка точности для системы
    h = l / n
    X = [x0 + i * h for i in range(n + 1)] # делим отрезок [x0, x0 + l] на n частей
    Y = [y0] # y(x0) = y0
    for i in range(n):
        xi = X[i]
        yi = Y[i]
        #k1 = f(xi, yi)
        #k2 = f(xi + h / 2, linearComb([yi, k1], [1, h / 2]))
        #k3 = f(xi + h / 2, linearComb([yi, k2], [1, h / 2]))
        #k4 = f(xi + h, linearComb([yi, k3], [1, h]))

        #k2 = f(xi + h / 2, yi + k1 * h / 2)
        #k3 = f(xi + h / 2, yi + k2 * h / 2)
        #k4 = f(xi + h, yi + k3 * h)




        k1 = f(xi, yi)
        lll = [yi[j] + k1[j] * h / 2 for j in [0, 1]]
        k2 = f(xi + h / 2, lll)
        lll = [yi[j] + k2[j] * h / 2 for j in [0, 1]]
        k3 = f(xi + h / 2, lll)
        lll = [yi[j] + k3[j] * h for j in [0, 1]]
        k4 = f(xi + h, lll)

        print(f"i = {i}, xi = {xi}")
        print(k1)
        print(k2)
        print(k3)
        print(k4)
        print()













        lll = linearComb([k1, k2, k3, k4], [1, 2, 2, 1])
        Y.append(linearComb([yi, lll], [1, h/6]))
    return X, Y


def getReal(f, x0, l):
    n = 40
    h = l / n
    X = [x0 + i * h for i in range(n + 1)] # делим ось x на отрезки
    Y = [f(x) for x in X]
    return X, Y



def getReal_sys(f, x0, l):
    n = 40
    h = l / n
    X = [x0 + i * h for i in range(n + 1)] # делим ось x на отрезки
    Y = [f(x) for x in X]
    return X, Y
