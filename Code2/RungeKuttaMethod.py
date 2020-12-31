
# Метод Рунге-Кутта 2 порядка точности:
def rk2(f, x0, y0, l, n):
    h = l / n
    # делим отрезок [x0, x0 + l] на n частей:
    X = [x0 + i * h for i in range(n + 1)]
    Y = [y0] # y(x0) = y0
    for i in range(n):
        xi = X[i]
        yi = Y[i]
        # Вычисление вспомогательных коэффициентов:
        k1 = f(xi, yi)
        k2 = f(xi + h, yi + k1 * h)
        # По рекурентной формуле вычисляем следующий y:
        Y.append(yi + h * (k1 + k2) / 2)
    return X, Y
    
    
# Метод Рунге-Кутта 4 порядка точности:
def rk4(f, x0, y0, l, n):
    h = l / n
    # делим отрезок [x0, x0 + l] на n частей:
    X = [x0 + i * h for i in range(n + 1)]
    Y = [y0] # y(x0) = y0
    for i in range(n):
        xi = X[i]
        yi = Y[i]
        # Вычисление вспомогательных коэффициентов:
        k1 = f(xi, yi)
        k2 = f(xi + h / 2, yi + k1 * h / 2)
        k3 = f(xi + h / 2, yi + k2 * h / 2)
        k4 = f(xi + h, yi + k3 * h)
        # По рекурентной формуле вычисляем следующий y:
        Y.append(yi + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6)
    return X, Y


# Функция для получения точек графика реальной функции:
def getReal(f, x0, l):
    n = 40
    h = l / n
    # делим отрезок [x0, x0 + l] на n частей:
    X = [x0 + i * h for i in range(n + 1)]
    Y = [f(x) for x in X]
    return X, Y


# Метод Рунге-Кутта 4 порядка точности для системы:
def rk4_sys(fs, x0, y0, l, n):
    h = l / n
    # делим отрезок [x0, x0 + l] на n частей:
    X = [x0 + i * h for i in range(n + 1)]
    Y = [y0] # y(x0) = y0
    indexGen = range(len(y0))
    f = lambda x, y: [fs[0](x, y), fs[1](x, y)]
    for i in range(n):
        xi = X[i]
        yi = Y[i]
        # Вычисление вспомогательных коэффициентов:
        k1 = f(xi, yi)
        tmp = [yi[j] + k1[j] * h / 2 for j in indexGen]
        k2 = f(xi + h / 2, tmp)
        tmp = [yi[j] + k2[j] * h / 2 for j in indexGen]
        k3 = f(xi + h / 2, tmp)
        tmp = [yi[j] + k3[j] * h for j in indexGen]
        k4 = f(xi + h, tmp)
        # По рекурентной формуле вычисляем следующий y:
        tmp = [k1[j] + 2 * (k3[j] + k3[j]) + k4[j] for j in indexGen]
        Y.append([yi[j] + tmp[j] * h / 6 for j in indexGen])
    return X, Y


