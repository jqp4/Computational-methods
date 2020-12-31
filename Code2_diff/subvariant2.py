
# Подключаем модуль для качественного отображения графиков:
import matplotlib.pyplot as plt

# Подключаем файл с описанными методами:
from DiffEq2Ord import DifferentialEquation, finiteDifferenceMethod, getReal

# Некоторые константы для отображения графиков:
WINDOW_WIDTH = 8
WINDOW_HEIGHT = 6
COLORS = ['c', 'b', 'r', 'k', 'm']

# Некоторые полезные функции:
exp = lambda x: 2.718281828459045 ** x

def boundaryValueProblem(x0, xn, diffEq, ns, yreal=None):
    # Решаем Краевую задачу
    fig = plt.figure()
    if yreal != None:
        X, Y = getReal(yreal, x0, xn)
        plt.plot(X, Y, marker = 'o', color='greenyellow', label='Точное решение')
    for n, c in zip(ns, COLORS):
        X, Y = finiteDifferenceMethod(diffEq, x0, xn, n)
        plt.plot(X, Y, color=c, label=f'{n} шагов')
    
    # Оформляем графики:
    plt.gcf().canvas.set_window_title('Подвариант 2. Для продолжения закройте это окно')
    plt.title('Метод конечных разностей')
    fig.set_figheight(WINDOW_HEIGHT)
    fig.set_figwidth(WINDOW_WIDTH)
    plt.legend()
    plt.grid()  
    plt.show()


def main():
    # Вариант 8
    # Определяем начальные данные:
    x0 = 1.2
    xn = 1.5
    p = lambda x: 3
    q = lambda x: -1 / x
    f = lambda x: -x - 1
    sigma = [0, 2]
    gamma = [1, -1]
    delta = [1, 0.5]
    de = DifferentialEquation(p, q, f, sigma, gamma, delta)
    boundaryValueProblem(x0, xn, de, [25, 150, 700, 3500])

    # Тест для проверки метода:
    x0 = -1
    xn = 1
    p = lambda x: 2
    q = lambda x: 0
    f = lambda x: 0
    sigma = [1, 1]
    gamma = [0, 1]
    delta = [1, 2]
    de = DifferentialEquation(p, q, f, sigma, gamma, delta)
    yreal = lambda x: (-exp(2 - 2 * x) + 1 + 2 * exp(4)) / (1 + exp(4))
    boundaryValueProblem(x0, xn, de, [5, 15, 45], yreal)


main()