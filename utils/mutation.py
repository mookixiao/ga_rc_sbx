import random


# 多项式变异
def mutation(population, p_mut, V, min_val, max_val, eta_m):
    for i in range(len(population)):
        for j in range(V):
            r = random.random()
            if r <= p_mut:
                num = population[i][j]
                num_low = min_val[j]
                num_up = max_val[j]
                delta_1 = 1.0 * (num - num_low) / (num_up - num_low)
                delta_2 = 1.0 * (num_up - num) / (num_up - num_low)

                u = random.random()
                temp_1 = 1.0 / (eta_m + 1.0)
                if u <= 0.5:
                    temp_2 = 1.0 - delta_1
                    temp_3 = 2.0 * u + (1.0 - 2.0 * u) * temp_2 ** (eta_m + 1.0)
                    delta = temp_3 ** temp_1 - 1.0
                else:
                    temp_2 = 1.0 - delta_2
                    temp_3 = 2.0 * (1.0 - u) + 2.0 * (u - 0.5) * temp_2 ** (eta_m + 1.0)
                    delta = 1.0 - temp_3 ** temp_1
                num = num + delta * (num_up - num_low)
                num = min(num_up, max(num, num_low))
                population[i][j] = num