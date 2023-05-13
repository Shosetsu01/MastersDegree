import numpy as np

from Fletcher_Reeves_Method import Fletcher_Reeves_method
from Nelder_Mead_method import nelder_mead_method

def P(x, r, equations, inequalities):
    sum_equations = np.sum([g(x) for g in equations]) ** 2
    array_g_x_inequalities = np.vectorize(lambda g, x: g(x), signature='(),(n)->()',)(inequalities, x)
    array_g_x_inequalities[array_g_x_inequalities < 0] = 0
    sum_inequalities = (array_g_x_inequalities ** 2).sum()
    ans = r / 2 * (sum_equations + sum_inequalities)
    return ans 

def step2(x, r, bind_P, f):
    # n = 2
    # E = 0.00001
    # a, b, y = 1, 0.5, 2
    # F_Rm = lambda x, f : nelder_mead_method(a, b, y, E, n, f, x0=x)
    e1 = 0.01
    e2 = 0.015
    M = 100
    F_Rm = lambda x, f : Fletcher_Reeves_method(x, e1, e2, M, f)
    F = lambda x: f(x) + bind_P(x, r)
    x = F_Rm(x, F)
    return x

def penalty_method(r, C, f, e, equations, inequalities):
    bind_P = lambda x, r: P(x, r, equations, inequalities)
    x = [-100, 200]
    x = np.array(x, dtype=float)
    x = step2(x, r, bind_P, f)
    r = r * C
    while abs(bind_P(x, r)) > e :
        x = step2(x, r, bind_P, f)
        r = r * C
    return x

if __name__ == "__main__":
    f = lambda x : x[0] ** 2 + x[1] ** 2
    #equations = [lambda x: x[0] - 1]
    #inequalities = [lambda x: x[0] + x[1] - 2]
    #equations = [lambda x: x[0] - 1]
    equations = []
    inequalities = [ lambda x: x[0] + x[1] - 2, lambda x: -x[0] + 1]
    #inequalities = [lambda x: x[0] ** 2 + x[1] ** 2 - 2 ]
    r = 1
    C = 10
    e = 0.000000000001
    # bounds = [(None, -0.6), (None, -0.6)]
    # bounds = np.array(bounds, dtype=[('right', float), ('left', float)])
    ans = penalty_method(r, C, f , e, equations, inequalities,)
    
    print(ans)