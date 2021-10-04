import random

# 种群初始化
def population_init(population, N, V, min_val, max_val):
    range_val=[max_val[i] - min_val[i] for i in range(V)]

    for i in range(N):
        item=[]
        for j in range(V):
            val = random.uniform(0, 1) * range_val[j] + min_val[j]
            item.append(val)
        population.append(item)


if __name__ == "__main__":
    print("***测试群体初始化函数，个体数10，每个个体基因数2，第一个基因位于[1, 2]，第二个基因位于[2, 3]")

    population = []
    population_init(population, 10, 2, (1, 2), (2, 3))
    for i, item in enumerate(population):
        print("item " + str(i + 1) + ": " + str(item[0]) + ", " + str(item[1]))