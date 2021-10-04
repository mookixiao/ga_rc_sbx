# 计算适应函数值
def cal_fit_value(population, fit_val, fit_func):
    del fit_val[:]

    for item in population:
        fit_val.append(fit_func(item))


if __name__ == "__main__":
    print("***测试适应度计算函数，假设三个个体分别为[2, 3], [5, 6], [8, 9]，适应度函数为x^2+y^2")

    def fit_func(item):
        return item[0] ** 2 + item[1] ** 2

    population = [[2, 3],
                  [5, 6],
                  [8, 9]]
    fit_val = []
    cal_fit_value(population, fit_val, fit_func)
    for i in range(len(fit_val)):
        print("item [" + str(population[i][0]) + ", " + str(population[i][1]) + "]: " + str(fit_val[i]))