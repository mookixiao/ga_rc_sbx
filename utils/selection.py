import copy
import random


# 轮盘赌选择下一代
def selection(population, fit_val):
    s = sum(fit_val)
    temp = [k / s for k in fit_val]
    temp2 = []

    s2 = 0
    for k in temp:
        s2 = s2 + k
        temp2.append(s2)

    temp3 = []
    for _ in range(len(population)):
        r = random.random()
        for i in range(len(temp2)):
            if r <= temp2[i]:
                temp3.append(i)
                break

    temp4 = []
    temp5 = []
    for i in temp3:
        temp4.append(population[i])
        temp5.append(fit_val[i])
    population[:] = temp4
    fit_val[:] = temp5