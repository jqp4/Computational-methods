
# Библиотреки для качествоенного отображения графиков:
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from mpl_toolkits.mplot3d import Axes3D

# Подклбчаем файл с описанными методами:
from DiffEq2Ord import DifferentialEquation, lll

# Некоторые константы для отображения графиков:
WINDOW_WIDTH = 8
WINDOW_HEIGHT = 6
COLORS = ['c', 'b', 'r', 'k', 'm']





def main():
    print('\n' * 30)
    # Вариант 8
    # Определяем начальные данные:
    x0 = 0.2
    xn = 0.5
    p = lambda x: 2
    q = lambda x: -1 / x
    f = lambda x: 3
    sigma = [1, 0.5]
    gamma = [0, -1]
    delta = [2, 1]
    de = DifferentialEquation(p, q, f, sigma, gamma, delta)

    ns = [50]
    fig, ax = plt.subplots()
    for n, c in zip(ns, COLORS):
        X, Y = lll(de, x0, xn, n)
        plt.plot(X, Y, color=c, label=f'{n} шагов')
    





    # Оформляем графики:
    #plt.gcf().canvas.set_window_title('Для продолжения закройте это окно')
    #plt.title('Метод Рунге-Кутта 4-го порядка точности для системы')
    fig.set_figheight(WINDOW_HEIGHT)
    fig.set_figwidth(WINDOW_WIDTH)
    plt.legend()
    plt.grid()  
    plt.show()


main()