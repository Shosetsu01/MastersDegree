import numpy as np
import matplotlib.pyplot as plt

def step_2_3(dots, n, dtype, plot, array_dots):
    dots = np.array(dots, dtype=dtype) 
    dots = np.sort(dots, order='f_x')[::-1]
    if plot:
        array_dots.append(list(dots['x'].copy()))
    x_n2 = 1 / n * (np.sum(dots[1:]['x'],  axis=0)) # центр тяжести
    return dots, x_n2


def nelder_mead_method(a, b, y, E, n, f, dots=None, plot=False, x0=None, h=10):
    array_dots = []
    dtype = [('f_x', float), ('x', np.float64, (n,))]
    if  x0 is not None:
        dots = np.full((n + 1, n), x0)
        np.fill_diagonal(dots, dots.diagonal() + h)
    if dots is None:
        dots = np.random.random((n + 1, n))
    dots = [(f(x), x) for x in dots]
    dots, x_n2 = step_2_3(dots, n, dtype, plot, array_dots)
    while np.sqrt(np.sum((dots['f_x'] - f(x_n2)) ** 2) / (n + 1)) >= E:
        x_n3 = x_n2 + a * (x_n2 - dots[0]['x']) # отражения
        f_xn3 = f(x_n3)
        if f_xn3 <= dots[-1]['f_x']:
            x_n4 = x_n2 + y * (x_n3 - x_n2) # растяжение
            if f(x_n4) < dots[-1]['f_x']:
                tmp = x_n4
            else:
                tmp = x_n3
            dots[0] = np.array((f(tmp), tmp), dtype=dtype) 
        elif dots[1]['f_x'] < f_xn3 <= dots[0]['f_x']:
            tmp = x_n2 + b * (dots[0]['x'] - x_n2) # сжатия
            dots[0] = np.array((f(tmp), tmp), dtype=dtype) 
        elif dots[-1]['f_x'] < f_xn3 <= dots[1]['f_x']:
            dots[0] = np.array((f(x_n3), x_n3), dtype=dtype) 
        elif f_xn3 > dots[0]['f_x']:
            dots = dots[-1]['x'] + 0.5 * (dots['x'] - dots[-1]['x'])
            dots = [(f(x), x) for x in dots ]
        dots, x_n2 = step_2_3(dots, n, dtype, plot, array_dots)
    if plot:
        return array_dots, dots[-1]['x']
    return dots[-1]['x']



if __name__ == "__main__":
    n = 2
    f = lambda x : 4 * (x[0] - 5) ** 2 + (x[1] - 6) ** 2
    E = 0.2
    a, b, y = 1, 0.5, 2
    dots = np.array([[8,9], [10, 11], [8, 11]], dtype=float)
    ans = nelder_mead_method(a, b, y, E, n, f, dots)
    print(f(ans), f((5, 6.25)))
    array_dots, ans = nelder_mead_method(a, b, y, E, n, f, dots, plot=True)
    X = []
    Y = []

    for dots in array_dots:
        for x, y in dots:
            X.append(x)
            Y.append(y)
        X.append(dots[0][0])
        Y.append(dots[0][1])

    plt.plot(X, Y, marker=".", c="g")
    plt.scatter(5, 6.25, color='orange', s=40, marker='o')
    plt.show()
