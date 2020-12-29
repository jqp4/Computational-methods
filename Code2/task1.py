import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from RungeKuttaMethod import rk2, rk4, getReal



width = 10
height = 6
colors = ['c', 'b', 'r', 'k', 'm', 'g']
dind = 20



def main_old():
    width = 10
    height = 6
    colors = ['c', 'b', 'r', 'k', 'm', 'g']

    x0 = 0
    y0 = 1
    l = 5
    #f = lambda x, y: x * y * (1 - x) if y else 1
    f = lambda x, y: x * y * (1 - x)
    ymax = 1.5
    dind = 25

    for name, rk, ns in zip([2, 4], [rk2, rk4], [[15, 25, 50], [10, 15, 25]]):
        fig, ax = plt.subplots()
        for n, c in zip(ns, colors):
            X, Y = rk(f, x0, y0, l, n)
            plt.plot(X, Y, color=c, label=f'{n} итераций')
        
        # Устанавливаем отступ от осей:
        ax.set_xlim([x0 - l / dind, x0 + l + l / dind])
        ax.set_ylim([0 - ymax / dind, ymax + ymax / dind])

        # Устанавливаем интервалы делений на осях x и y:
        ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

        # Оформляем графики:
        plt.title(f'Метод Рунге-Кутта {name}-го порядка точности')
        plt.legend(loc='lower left')
        fig.set_figheight(height)
        fig.set_figwidth(width)
        plt.grid()  
        plt.show()



def Test1():
    x0 = 0
    y0 = 10
    l = 10
    f = lambda x, y: -y - x ** 2
    exp = lambda x: 2.718281828459045 ** x
    yreal = lambda x: -x ** 2 + 2 * x - 2 + 12 * exp(-x)
    ymin = yreal(x0 + l)
    xind = l / dind
    yind = (y0 - ymin) / dind
    ns = [5, 10, 25]

    for MethodIndex, rk in zip([2, 4], [rk2, rk4]):
        fig, ax = plt.subplots()
        X, Y = getReal(yreal, x0, l)
        plt.plot(X, Y, marker = 'o', color='greenyellow', label='Точное решение')
        for n, c in zip(ns, colors):
            X, Y = rk(f, x0, y0, l, n)
            plt.plot(X, Y, color=c, label=f'{n} шагов')
        
        # Устанавливаем границы осей:
        ax.set_xlim([x0 - xind, x0 + l + xind])
        ax.set_ylim([ymin - yind, y0 + yind])

        # Оформляем графики:
        plt.title(f'Метод Рунге-Кутта {MethodIndex}-го порядка точности')
        plt.legend(loc='lower left')
        fig.set_figheight(height)
        fig.set_figwidth(width)
        plt.grid()  
        plt.show()









def Test2():
    x0 = 0
    y0 = 10
    l = 10
    f = lambda x, y: -y - x ** 2
    #ymax = 1.5
    exp = lambda x: 2.718281828459045 ** x
    yreal = lambda x: -x ** 2 + 2 * x - 2 + 12 * exp(-x)

    for name, rk, ns in zip([2, 4], [rk2, rk4], [[5, 10, 25], [5, 10, 25]]):
        fig, ax = plt.subplots()
        X, Y = getReal(yreal, x0, l)
        plt.plot(X, Y, marker = 'o', color='greenyellow', label='Точное решение')
        for n, c in zip(ns, colors):
            X, Y = rk(f, x0, y0, l, n)
            plt.plot(X, Y, color=c, label=f'{n} итераций')
        
        
        # Устанавливаем отступ от осей:
        #ax.set_xlim([x0 - l / dind, x0 + l + l / dind])
        #ax.set_ylim([0 - ymax / dind, ymax + ymax / dind])

        # Устанавливаем интервалы делений на осях x и y:
        #ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
        #ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
        #ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
        #ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

        # Оформляем графики:
        plt.title(f'Метод Рунге-Кутта {name}-го порядка точности')
        plt.legend(loc='lower left')
        fig.set_figheight(height)
        fig.set_figwidth(width)
        plt.grid()  
        plt.show()

def main():
    Test1()

main()