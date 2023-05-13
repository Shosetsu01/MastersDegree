from Sven_method import sven_method
import matplotlib.pyplot as plt

def dichotomy_method(E, l, f, a, b):

    while abs(a - b) > l:
        y = (a + b - E) / 2
        z = (a + b + E) / 2
        if f(y) > f(z):
            a = y
        else:
            b = z

    return (a + b) / 2


if __name__ == "__main__":
    f = lambda x : 2 * x ** 2 - 12 * x
    E = 0.000001
    l = 0.00001 # l < E
    x0 = 5 
    h = 5
    segment = sven_method(x0, h, f)
    if segment:
        a, b = segment 
    ans = dichotomy_method(E, l, f, a, b)
    print(ans)
