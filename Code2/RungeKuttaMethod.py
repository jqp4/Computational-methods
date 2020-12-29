

def rk2(f, x0, y0, l, n):
    # Метод Рунге-Кутта 2 порядка точности
    h = l / n
    X = [x0 + i * h for i in range(n + 1)] # делим ось x на отрезки
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
    X = [x0 + i * h for i in range(n + 1)] # делим ось x на отрезки
    Y = [y0] # y(x0) = y0
    for i in range(n):
        xi = X[i]
        yi = Y[i]
        k1 = f(xi, yi)
        k2 = f(xi + h / 2, yi + k1 * h / 2)
        k3 = f(xi + h / 2, yi + k2 * h / 2)
        k4 = f(xi + h, yi + k2 * h)
        # По рекурентной формуле вычисляем следующий y:
        Y.append(yi + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6)
    return X, Y


def getReal(f, x0, l):
    n = 40
    h = l / n
    X = [x0 + i * h for i in range(n + 1)] # делим ось x на отрезки
    Y = [f(x) for x in X]
    return X, Y
