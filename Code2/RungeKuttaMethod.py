

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


def getReal(f, x0, l):
    n = 40
    h = l / n
    X = [x0 + i * h for i in range(n + 1)] # делим ось x на отрезки
    Y = [f(x) for x in X]
    return X, Y



def rk4_sys(fs, x0, y0, l, n):
    # Метод Рунге-Кутта 4 порядка точности для системы
    h = l / n
    X = [x0 + i * h for i in range(n + 1)] # делим отрезок [x0, x0 + l] на n частей
    Y = [y0] # y(x0) = y0
    indexGen = range(len(y0))
    f = lambda x, y: [fs[0](x, y), fs[1](x, y)]
    for i in range(n):
        xi = X[i]
        yi = Y[i]

        k1 = f(xi, yi)
        tmp = [yi[j] + k1[j] * h / 2 for j in indexGen]
        k2 = f(xi + h / 2, tmp)
        tmp = [yi[j] + k2[j] * h / 2 for j in indexGen]
        k3 = f(xi + h / 2, tmp)
        tmp = [yi[j] + k3[j] * h for j in indexGen]
        k4 = f(xi + h, tmp)

        #print(f"\ni = {i}, xi = {xi}")
        #for ki, k in enumerate([k1, k2, k3, k4]):
        #    print("{0} : {1:6.3f}, {2:6.3f}".format(ki, k[0], k[1]))

        # По рекурентной формуле вычисляем следующий y:
        tmp = [k1[j] + 2 * (k3[j] + k3[j]) + k4[j] for j in indexGen]
        Y.append([yi[j] + tmp[j] * h / 6 for j in indexGen])
    return X, Y


