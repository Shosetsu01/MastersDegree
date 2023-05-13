import random
import numpy as np
import matplotlib.pyplot as plt
# from Sven_method import sven_method
# from dichotomy_method import dichotomy_method

def sven_method(x0, h, f):
    left_f_x0, f_x0, rigth_f_x0 = f(x0 - h), f(x0), f(x0 + h)
    if left_f_x0 >= f_x0 <= rigth_f_x0:
        return (x0 - h, x0 + h)
    if left_f_x0 <= f_x0 >= rigth_f_x0:
        return None 
    if left_f_x0 >= f_x0 >= rigth_f_x0:
        x1 = x0 + h 
    if left_f_x0 <= f_x0 <= rigth_f_x0:
        x1 = x0 - h
        h = -h
    h *= 2
    while f(x1) < f(x0):
        tmp = x0 
        x0 = x1
        x1 = x0 + h
        h *= 2

    if h > 0:
        return(tmp, x1)
    return (x1, tmp)

def dichotomy_method(E, l, f, a, b):

    while abs(a - b) > l:
        y = (a + b - E) / 2
        z = (a + b + E) / 2
        if f(y) > f(z):
            a = y
        else:
            b = z

    return (a + b) / 2

def steepest_gradient_descent_method(x, e1, e2, M, f, plot=False,):
    dx = 0.0000001
    df = lambda x : grad_f(dx, x, f)
    array_dots = []
    k = 0
    g_f = df(x)
    while np.linalg.norm(g_f, ord=2)  >= e1 and k < M:
        t = f_t(x, g_f, f)
        tmp = x
        x = x - t * g_f
        if plot:
            array_dots.append(x.copy())
        if np.linalg.norm(x - tmp, ord=2) < e2  and abs( f(x) - f(tmp)) < e2:
            break
        k +=1
        g_f = df(x)
    return x
    


def grad_f(dx, x, f):
    array_x = []
    for i in range(len(x)):
        tmp  = x.copy()
        tmp[i] = tmp[i] - dx
        tmp2 = x.copy()
        tmp2[i] = tmp2[i] + dx
        array_x.append([tmp2, tmp])
    array_x = np.array(array_x)
    tmp = [(f(cloum[0]) - f(cloum[1])) / (2 * dx) for cloum in array_x]
    return np.array(tmp)

def f_t(x, g_f, f,):
    t = lambda t: f(x - g_f * t)
    E = 0.000000001
    l = 0.00001
    random.seed( version=2)
    h = random.uniform(0.1, 1000)
    x0 = random.uniform(-1000, 1000)
    segment = sven_method(x0, h, t)
    if segment:
        a, b = segment 
    ans = dichotomy_method(E, l, t, a, b)
    return ans




if __name__ == "__main__":
    n = 2
    dx = 0.005
    f = lambda x : 2 * x[0] ** 2 + x[0] * x[1] + x[1] ** 2  
    df = lambda x : grad_f(dx, x, f)
    x0 = [0.5, 1.0]
    x0 = np.array(x0)
    e1 = 0.1
    e2 = 0.15
    M = 1
    ans = steepest_gradient_descent_method(x0, e1, e2, M, f)
    print(ans)
