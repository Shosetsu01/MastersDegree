# Оптимизация колонии Ant для решения проблемы TSP
import numpy as np
import random as rd

def lengthCal(antPath,distmat):         # Рассчитать расстояние
    length = []
    dis = 0
    for i in range(len(antPath)):
        for j in range(len(antPath[i]) - 1):
            dis += distmat[antPath[i][j]][antPath[i][j + 1]]
        dis += distmat[antPath[i][-1]][antPath[i][0]]
        length.append(dis)
        dis = 0
    return length

distmat = np.array([[0,35,29,67,60,50,66,44,72,41,48,97],
                 [35,0,34,36,28,37,55,49,78,76,70,110],
                 [29,34,0,58,41,63,79,68,103,69,78,130],
                 [67,36,58,0,26,38,61,80,87,110,100,110],
                 [60,28,41,26,0,61,78,73,103,100,96,130],
                 [50,37,63,38,61,0,16,64,50,95,81,95],
                 [66,55,79,61,78,16,0,49,34,82,68,83],
                 [44,49,68,80,73,64,49,0,35,43,30,62],
                 [72,78,103,87,103,50,34,35,0,47,32,48],
                 [41,76,69,110,100,95,82,43,47,0,26,74],
                 [48,70,78,100,96,81,68,30,32,26,0,58],
                 [97,110,130,110,130,95,83,62,48,74,58,0]])

antNum = 12                   # Не номер
alpha = 1                     # Фактор важности феромона
beta = 3                      # Фактор важности эвристической функции
pheEvaRate = 0.3              # Скорость испарения феромона
cityNum = distmat.shape[0]
pheromone = np.ones((cityNum,cityNum))                   # Феромоновая матрица
heuristic = 1 / (np.eye(cityNum) + distmat) - np.eye(cityNum)       # Матрица эвристической информации, дубль 1 / дизмат
iter,itermax = 1,1000                       # Итерации

while iter < itermax:
    antPath = np.zeros((antNum, cityNum)).astype(int) - 1   # Путь муравья
    firstCity = [i for i in range(12)]
    rd.shuffle(firstCity)          # Случайно назначьте начальный город для каждого муравья
    unvisted = []
    p = []
    pAccum = 0
    for i in range(len(antPath)):
        antPath[i][0] = firstCity[i]
    for i in range(len(antPath[0]) - 1):       # Постепенно обновляйте следующий город, в который собирается каждый муравей
        for j in range(len(antPath)):
            for k in range(cityNum):
                if k not in antPath[j]:
                    unvisted.append(k)
            for m in unvisted:
                pAccum += pheromone[antPath[j][i]][m] ** alpha * heuristic[antPath[j][i]][m] ** beta
            for n in unvisted:
                p.append(pheromone[antPath[j][i]][n] ** alpha * heuristic[antPath[j][i]][n] ** beta / pAccum)
            roulette = np.array(p).cumsum()               # Создать рулетку
            r = rd.uniform(min(roulette), max(roulette))
            for x in range(len(roulette)):
                if roulette[x] >= r:                      # Используйте метод рулетки, чтобы выбрать следующий город
                    antPath[j][i + 1] = unvisted[x]
                    break
            unvisted = []
            p = []
            pAccum = 0
    pheromone = (1 - pheEvaRate) * pheromone            # Феромон летучий
    length = lengthCal(antPath,distmat)
    for i in range(len(antPath)):
        for j in range(len(antPath[i]) - 1):
            pheromone[antPath[i][j]][antPath[i][j + 1]] += 1 / length[i]     # Обновление феромона
        pheromone[antPath[i][-1]][antPath[i][0]] += 1 / length[i]
    iter += 1
print("Кратчайшее расстояние:")
print(min(length))
print("Самый короткий путь:")
print(antPath[length.index(min(length))])
