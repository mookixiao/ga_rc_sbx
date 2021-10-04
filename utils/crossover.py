import random


# 仿二进制交叉
def crossover(population, p_cross, V, min_val, max_val, eta_c):
    for i in range(0, len(population), 2):
        if random.random() > p_cross:
            continue

        for j in range(V):
            num_low = min_val[j]
            num_up = max_val[j]
            item_1 = population[i][j]
            item_2 = population[i + 1][j]
            u = random.random()
            if u <= 0.5:
                beta = (2 * u) ** (1.0 / (eta_c + 1.0))
            else:
                beta = (0.5 / (1.0 - u)) ** (1.0 / (eta_c + 1.0))

            child_1 = 0.5*((1 + beta) * item_1 + (1 - beta) * item_2)
            child_2 = 0.5*((1 - beta) * item_1 + (1 + beta) * item_2)
            child_1 = min(max(child_1, num_low), num_up)
            child_2 = min(max(child_2, num_low), num_up)

            population[i][j] = child_1
            population[i + 1][j] = child_2