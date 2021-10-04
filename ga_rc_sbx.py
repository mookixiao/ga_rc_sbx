import math
import time
from utils.population_init import population_init
from utils.cal_fit_val import cal_fit_value
from utils.selection import selection
from utils.crossover import crossover
from utils.mutation import mutation


# 初始化参数
N_lst = [20, 40, 60, 80, 100]
G_lst = [100, 200, 400, 500]
V = 2
min_val = (-5.12, -5.12)  # x y
max_val = (5.12, 5.12)    # x y
population = []
p_cross = 0.75
p_mut = 0.3
eta_c = 2
eta_m = 2

# 目标函数值列表
fit_val=[]

# 目标函数
def fit_func(item):
    x = item[0]
    y = item[1]
    fit_value = 21.5 + x * math.sin(4 * math.pi * x) + y * math.sin(20 * math.pi * y)
    return fit_value


if __name__ == "__main__":
    for N in N_lst:
        start_time = time.time()
        for G in G_lst:
            population_init(population, N, V, min_val, max_val)
            cal_fit_value(population, fit_val, fit_func)

            for i in range(G):  # 遗传G代
                selection(population, fit_val)
                crossover(population, p_cross, V, min_val, max_val, eta_c)
                mutation(population, p_mut, V, min_val, max_val, eta_m)

                cal_fit_value(population, fit_val, fit_func)
                max_fit_val = max(fit_val)
                avg_fit_val = sum(fit_val) / N

            end_time = time.time()
            print("%.4f " % (end_time - start_time), end="")

        print()