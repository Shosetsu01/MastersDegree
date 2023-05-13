import numpy as np
import matplotlib.pyplot as plt
from steepest_gradient_descent_method import f_t, grad_f, steepest_gradient_descent_method

def Fletcher_Reeves_method(x0, e1, e2, M, f, df, plot=False):
    array_dots = []
    k = 1
    if plot:
        array_dots.append(x0.copy())
    x = steepest_gradient_descent_method(x0, e1, e2, 1, f, df)
    g_f = df(x)
    prev_x = x0
    d = -df(x0)
    prev_g_f = -d
    if plot:
        array_dots.append(x.copy())
    if np.linalg.norm(x - x0, ord=2) < e2  and abs( f(x) - f(x0)) < e2:
        return x
    while np.linalg.norm(g_f, ord=2)  >= e1 and k < M:
        b = (np.linalg.norm(g_f, ord=2) / np.linalg.norm(prev_g_f, ord=2)) ** 2
        d = -g_f + b * d
        t = f_t(x, -d, f)
        prev_x = x
        prev_g_f = g_f
        x = x + t * d
        if plot:
            array_dots.append(x.copy())
        if np.linalg.norm(x - prev_x, ord=2) < e2  and abs( f(x) - f(prev_x)) < e2:
            break
        k +=1
        g_f = df(x)
      
    if plot:
        return x, array_dots
   
    return x



if __name__ == "__main__":
    n = 2
    dx = 0.0000001
    f = lambda x : 2 * x[0] ** 2 + x[0] * x[1] + x[1] ** 2  
    df = lambda x : grad_f(dx, x, f)
    x0 =[0.5, 1.0]
    x0 = np.array(x0)
    g = df(x0)
    e1 = 0.1
    e2 = 0.15
    M = 10
    ans = Fletcher_Reeves_method(x0, e1, e2, M, f, df)
    plot = True
    if plot: 
    
        X = []
        Y = []

        ans, array_dots = Fletcher_Reeves_method(x0, e1, e2, M, f, df, plot)
        for x, y in array_dots:
            X.append(x)
            Y.append(y)
        

        plt.plot(X, Y, marker=".", c="g")
        plt.show()

    print(ans)
