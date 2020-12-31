
# Библиотреки для качествоенного отображения графиков:
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from mpl_toolkits.mplot3d import Axes3D

# Подклбчаем файл с описанными методами:
from RungeKuttaMethod import rk2, rk4, getReal, rk4_sys

# Некоторые константы для отображения графиков:
WINDOW_WIDTH = 8
WINDOW_HEIGHT = 6
COLORS = ['c', 'b', 'r', 'k', 'm']


# Задача Коши
def Test1():
    # Вариант 1 - 3
    # Определяем начальные данные:
    x0 = 0
    y0 = 10
    l = 10
    f = lambda x, y: -y - x ** 2
    exp = lambda x: 2.718281828459045 ** x
    yreal = lambda x: -x ** 2 + 2 * x - 2 + 12 * exp(-x)
    # Определяем значения для постоения графика:
    ymin = yreal(x0 + l)
    dind = 20
    xind = l / dind
    yind = (y0 - ymin) / dind

    # Решаем задачу Коши методом Рунге-Кутта 2 и 4 порядка точности:
    ns = [5, 10, 25]
    for MethodIndex, rk in zip([2, 4], [rk2, rk4]):
        fig, ax = plt.subplots()
        X, Y = getReal(yreal, x0, l)
        plt.plot(X, Y, marker = 'o', color='greenyellow', label='Точное решение')
        for n, c in zip(ns, COLORS):
            X, Y = rk(f, x0, y0, l, n)
            plt.plot(X, Y, color=c, label=f'{n} шагов')
        
        # Устанавливаем границы осей:
        ax.set_xlim([x0 - xind, x0 + l + xind])
        ax.set_ylim([ymin - yind, y0 + yind])

        # Оформляем графики:
        plt.gcf().canvas.set_window_title('Для продолжения закройте это окно')
        plt.title(f'Метод Рунге-Кутта {MethodIndex}-го порядка точности')
        plt.legend(loc='lower left')
        fig.set_figheight(WINDOW_HEIGHT)
        fig.set_figwidth(WINDOW_WIDTH)
        plt.grid()  
        plt.show()


# Задача Коши для системы
def Test2():
    # Вариант 2 - 17
    # Определяем начальные данные:
    x0 = 0
    y0 = [1, 0.5]
    l = 6
    e = 2.718281828459045
    # using Euler's formula: e^ix = cosx + isinx
    sin = lambda a: (e ** (a * 1j)).imag
    f1 = lambda x, y: sin(1.4 * y[0] ** 2) - x + y[1]
    f2 = lambda x, y: x + y[0] - 2.2 * y[1] ** 2 + 1
    fs = [f1, f2]

    # Решаем задачу Коши для Системы методом Рунге-Кутта 4 порядка точности:
    ns = [10, 15, 45]
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    for n, c in zip(ns, COLORS):
        X, Y = rk4_sys(fs, x0, y0, l, n)
        Ydivided = [[y[i] for y in Y] for i in [0, 1]]
        ax.plot(X, Ydivided[0], Ydivided[1], color=c, label=f'{n} шагов')
    
    # Оформляем графики:
    plt.gcf().canvas.set_window_title('Для продолжения закройте это окно')
    plt.title('Метод Рунге-Кутта 4-го порядка точности для системы')
    fig.set_figheight(WINDOW_HEIGHT)
    fig.set_figwidth(WINDOW_WIDTH)
    ax.set_xlabel('X')
    ax.set_ylabel('U (Y[0])')
    ax.set_zlabel('V (Y[1])')
    plt.legend()
    plt.grid()  
    plt.show()


def main():
    Test1()
    Test2()


main()