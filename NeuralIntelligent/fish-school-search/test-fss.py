from fss.fss import FishSchoolSearch
import numpy as np
import matplotlib.pyplot as plt
import math
import visualization
import convergence



def cmp(point, max_val, fss_point, fss_max_value, fss):
    print("------------------------------------")
    print("теоритический максимум: ", point)
    print("значение в точке максимума: ", max_val)
    print("максимум найденный FSS: ", fss_point)
    print("значение в максимуме FSS: ", fss_max_value)
    print("|x' - x| (найденный FSS - теоретический максимум): ", max(np.abs(fss_point - point)))
    print("|f(x') - f(x)| (значение в максимуме FSS - теоретический максимум):", np.abs(fss_max_value - max_val))
    print("time: ", fss.time, "sec")
    print("------------------------------------")


def test_1():
    fss = FishSchoolSearch(
        lower_bound_point=[-10, -10],
        higher_bound_point=[10, 10],
        population_size=50,
        iteration_count=100,
        individual_step_start=2,
        individual_step_final=0.01,
        weight_scale=50,
        func=lambda x: -0.1 * (x[0] * x[0] + x[1] * x[1]) + 20,
    )

    # v = visualization.Visualization(fss.history())
    # v.start(saved=True, filename="test_1.mp4")
    f, x = fss.max()
    cmp(np.array([0,0]), 20, x, f, fss)
    c = convergence.Convergence(fss.history(), 20)
    c.show()

def test_2():
    fss = FishSchoolSearch(
        lower_bound_point=[-100, -100],
        higher_bound_point=[100, 100],
        population_size=50,
        iteration_count=300,
        individual_step_start=10,
        individual_step_final=0.01,
        weight_scale=50,
        func=lambda x: 10 * (np.sin(0.1*x[0]) + np.sin(0.1*x[1])) + 20,
    )

    v = visualization.Visualization(fss.history())
    v.start(saved=True, filename="test_2.mp4")
    f, x = fss.max()
    cmp(np.array([10*np.pi/2, 10*np.pi/2]), 40, x, f, fss)
    c = convergence.Convergence(fss.history(), 40)
    c.show()

# Функция Розенброка
def test_3():
    def rosenbrock_func(x, y):
        return (1 - x)*(1 - x) + 100*(y - x*x)*(y - x*x)

    fss = FishSchoolSearch(
        lower_bound_point=[-1, -1],
        higher_bound_point=[2, 2],
        population_size=50,
        iteration_count=100,
        individual_step_start=1,
        individual_step_final=0.01,
        weight_scale=50,
        func=lambda x: 200 - rosenbrock_func(x[0], x[1]),
    )

    f, x = fss.max()
    cmp(np.array([0, 0]), 200, x, f, fss)
    c = convergence.Convergence(fss.history(), 200)
    c.show()

# Функция Экли
def test_4():
    def ackley_func(x, y):
        return -20 * np.exp(-0.2*np.sqrt(0.5*(x*x + y*y))) \
               - np.exp(0.5*(np.cos(2*np.pi*x) + np.cos(2*np.pi*y))) + np.exp(1) + 20

    fss = FishSchoolSearch(
        lower_bound_point=[-10, -10],
        higher_bound_point=[10, 10],
        population_size=50,
        iteration_count=100,
        individual_step_start=3,
        individual_step_final=0.01,
        weight_scale=50,
        func=lambda x: 20 - ackley_func(x[0], x[1]),
    )

    # v = visualization.Visualization(fss.history())
    # v.start(saved=True, filename="test_4.mp4")
    f, x = fss.max()
    cmp(np.array([0, 0]), 20, x, f, fss)
    c = convergence.Convergence(fss.history(), 20)
    c.show()

# Гладкая функция
def test_5():
    def holder_func(x, y):
        return np.abs(np.sin(x)*np.cos(y)*np.exp(np.abs(1 - np.sqrt(x*x + y*y)/np.pi)))

    fss = FishSchoolSearch(
        lower_bound_point=[-10, -10],
        higher_bound_point=[10, 10],
        population_size=50,
        iteration_count=200,
        individual_step_start=5,
        individual_step_final=0.01,
        weight_scale=50,
        func=lambda x: holder_func(x[0], x[1]),
    )

    # v = visualization.Visualization(fss.history())
    # v.start(saved=True, filename="test_5.mp4")
    f, x = fss.max()
    cmp(np.array([8.05502, -9.66459]), 19.2085, x, f, fss)
    c = convergence.Convergence(fss.history(), 19.2085)
    c.show()

def test_7():
    fss = FishSchoolSearch(
        lower_bound_point=[-10, -10],
        higher_bound_point=[10, 10],
        population_size=50,
        iteration_count=100,
        individual_step_start=10,
        individual_step_final=0.01,
        weight_scale=100,
        func=lambda x: 10 * (np.sin(0.1*x[0]) + np.sin(0.1*x[1])) + 20,
    )

    # v = visualization.Visualization(fss.history())
    # v.start(saved=True, filename="test_7.mp4")
    f, x = fss.max()
    cmp(np.array([10*np.pi/2, 10*np.pi/2]), 40, x, f, fss)
    c = convergence.Convergence(fss.history(), 40)
    c.show()

def test_8():
    def function(x):
        f = 0
        for i in range(len(x) - 1):
            f += x[i] * math.sin(math.sqrt(abs(x[i] - x[i + 1] - 47))) - (x[i + 1] + 47) * math.sin(math.sqrt(abs(x[i + 1] + x[i] / 2 + 47)))
        return f

    fss = FishSchoolSearch(
        lower_bound_point=[-512, -512, -512, -512],
        higher_bound_point=[512, 512, 512, 512],
        population_size=1000,
        iteration_count=1000,
        individual_step_start=50,
        individual_step_final=10,
        weight_scale=50,
        func=lambda x: function(x),
    )

    f, x = fss.max()
    cmp(np.array([1, 1, 1, 1]), 512, x, f, fss)
    c = convergence.Convergence(fss.history(), 512)
    c.show()

def test_6():
    def func(x):
        return sum((1 + x[i])*(1 + x[i]) + 100*(x[i+1] - x[i]*x[i])*(x[i+1] - x[i]*x[i]) for i in range(1, len(x) - 1, 1))

    fss = FishSchoolSearch(
        lower_bound_point=[-1, -1, -1, -1, -1, -1],
        higher_bound_point=[2, 2, 2, 2, 2, 2],
        population_size=300,
        iteration_count=5000,
        individual_step_start=2,
        individual_step_final=0.01,
        weight_scale=100,
        func=lambda x: 500 - func(x),
    )

    f, x = fss.max()
    cmp(np.array([1, 1, 1, 1, 1, 1]), 500, x, f, fss)
    c = convergence.Convergence(fss.history(), 500)
    c.show()

if __name__ == '__main__':
    # test_1()
    # test_2()
    # test_3()
    # test_4()
    # test_5()
    test_6()
    # test_7()
    # test_8()
