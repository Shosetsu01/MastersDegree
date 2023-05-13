

from Fletcher_Reeves_Method import Fletcher_Reeves_method
import numpy as np
from Nelder_Mead_method import nelder_mead_method


def U(x, inequalities):
    array_g_x_inequalities = np.vectorize(lambda g, x: -g(x), signature='(),(n)->()')(inequalities, x)
    if array_g_x_inequalities.max() >= 0:
        return True
    return False


def P(x, r, equations, inequalities):
    sum_equations = np.sum([g(x) for g in equations]) ** 2
    array_g_x_inequalities = np.vectorize(lambda g, x: -g(x), signature='(),(n)->()',)(inequalities, x)
    if array_g_x_inequalities.max() > 0:
        sum_inequalities = np.log(array_g_x_inequalities).sum()
    else: 
        sum_inequalities = 0
    ans = 1 / (2.0 * r) * sum_equations - r * sum_inequalities
    return ans 

def step2(x, f, r, bind_P, F_Rm ):
    F = lambda x: f(x) + bind_P(x, r)
    return F_Rm(x, F)

def step2(x, r, bind_P,  f):
    # n = 2
    # E = 0.001
    # a, b, y = 1, 0.5, 2
    # F_Rm = lambda x, f : nelder_mead_method(a, b, y, E, n, f, x0=x)
    e1 = 0.1
    e2 = 0.15
    M = 10
    F_Rm = lambda x, f : Fletcher_Reeves_method(x, e1, e2, M, f)
    F = lambda x: f(x) + bind_P(x, r)
    x = F_Rm(x, F)
    return x

def combined_penalty_method(r, C, f , e, equations, inequalities):
    bind_P = lambda x, r: P(x, r, equations, inequalities)
    x = [-100, -100]
    x = np.array(x, dtype=float)
    tmp = step2(x, r, bind_P, f)
    if U(tmp, inequalities): 
        x = tmp
    r = r / C 
    while abs(bind_P(x, r)) > e:
        tmp = step2(x, r, bind_P, f)
        if U(tmp, inequalities): 
            x = tmp

        r = r / C   
    return x



if __name__ == "__main__":
    f = lambda x : x[0] ** 2 + x[1] ** 2
    #equations = [lambda x: x[0] - 1]
    #inequalities = [lambda x: x[0] + x[1] - 2]
    equations = [lambda x: x[0] - 1]
    inequalities = [ lambda x: x[0] + x[1] - 2]
    #inequalities = [lambda x: x[0] ** 2 + x[1] ** 2 - 2 ]
    r = 1
    C = 4
    e = 0.0001
    # bounds = [(None, -0.6), (None, -0.6)]
    # bounds = np.array(bounds, dtype=[('right', float), ('left', float)])
    ans = combined_penalty_method(r, C, f , e, equations, inequalities,)
    
    print(ans)
