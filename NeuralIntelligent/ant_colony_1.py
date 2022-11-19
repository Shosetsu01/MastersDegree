import numpy as np
import matplotlib.pyplot as plt
 
 
class ACO:
    def __init__(self, parameters):
        """
        Параметры оптимизации колонии муравьев 
        """
        # Инициализация
        self.NGEN = parameters[0]  # Итерации 
        self.pop_size = parameters[1]  # Численность колонии
        self.var_num = len(parameters[2])  # Количество переменных
        self.bound = []  # Область действия ограничений переменных
        self.bound.append(parameters[2])
        self.bound.append(parameters[3])
 
        self.pop_x = np.zeros((self.pop_size, self.var_num))  # Расположение всех муравьев
        self.g_best = np.zeros((1, self.var_num))  # Оптимальное положение глобальных муравьев
 
        # Поиск исходного глобального оптимального решения 0-го поколения
        temp = -1
        for i in range(self.pop_size):
            for j in range(self.var_num):
                self.pop_x[i][j] = np.random.uniform(self.bound[0][j], self.bound[1][j])
            fit = self.fitness(self.pop_x[i])
            if fit > temp:
                self.g_best = self.pop_x[i]
                temp = fit
 
    def fitness(self, ind_var):
        """
        Расчет индивидуального значения адаптации
        """
        x1 = ind_var[0]
        x2 = ind_var[1]
        x3 = ind_var[2]
        x4 = ind_var[3]
        y = x1 ** 2 + x2 ** 2 + x3 ** 3 + x4 ** 4
        return y
 
    def update_operator(self, gen, t, t_max):
        """
        Оператор обновления: Обновление позиции в соответствии с вероятностью
        """
        rou = 0.7   # Коэффициент испарения феромонов
        Q = 1       # Фактор важности феромона
        lamda = 1 / gen
        pi = np.zeros(self.pop_size)
        for i in range(self.pop_size):
            for j in range(self.var_num):
                pi[i] = (t_max - t[i]) / t_max
                # Местоположение
                if pi[i] < np.random.uniform(0, 1):
                    self.pop_x[i][j] = self.pop_x[i][j] + np.random.uniform(-1, 1) * lamda
                else:
                    self.pop_x[i][j] = self.pop_x[i][j] + np.random.uniform(-1, 1) * (
                                self.bound[1][j] - self.bound[0][j]) / 2

                if self.pop_x[i][j] < self.bound[0][j]:
                    self.pop_x[i][j] = self.bound[0][j]
                if self.pop_x[i][j] > self.bound[1][j]:
                    self.pop_x[i][j] = self.bound[1][j]
            # Обновление значения t
            t[i] = (1 - rou) * t[i] + Q * self.fitness(self.pop_x[i])
            # Обновление глобального оптимального значения
            if self.fitness(self.pop_x[i]) > self.fitness(self.g_best):
                self.g_best = self.pop_x[i]
        t_max = np.max(t)
        return t_max, t
 
    def main(self):
        popobj = []
        best = np.zeros((1, self.var_num))[0]
        for gen in range(1, self.NGEN + 1):
            if gen == 1:
                tmax, t = self.update_operator(gen, np.array(list(map(self.fitness, self.pop_x))),
                                     np.max(np.array(list(map(self.fitness, self.pop_x)))))
            else:
               tmax, t = self.update_operator(gen, t, tmax)
            popobj.append(self.fitness(self.g_best))
            print('___ Поколение {} ___'.format(str(gen)))
            print(self.g_best)
            print(self.fitness(self.g_best))
            if self.fitness(self.g_best) > self.fitness(best):
                best = self.g_best.copy()
            print('Лучшее расположение：{}'.format(best))
            print('Максимальное значение функции：{}'.format(self.fitness(best)))
        print("--- Окончание поиска ---")
 
        plt.figure()
        plt.title("Изображение 1")
        plt.xlabel("итерации", size=14)
        plt.ylabel("приспособленность", size=14)
        t = [t for t in range(1, self.NGEN + 1)]
        plt.plot(t, popobj, color='b', linewidth=2)
        plt.show()
 
 
if __name__ == '__main__':
    NGEN = 100 # Кол-во итераций
    popsize = 100  # Численность колонии 
    low = [1, 1, 1, 1] # Нижняя граница
    up = [50, 50, 50, 50] # Верхняя граница
    parameters = [NGEN, popsize, low, up]
    aco = ACO(parameters)
    aco.main()