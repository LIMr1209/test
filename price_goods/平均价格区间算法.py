# https://jingpeicomp.gitbooks.io/search-platform/content/algorithm/number_section.html
import numpy as np
import csv

data = []
with open('price (3).csv')as f:
    f_csv = csv.reader(f)
    for i, row in enumerate(f_csv):
        if i > 1:
            data.append(int(float(row[2])))
data.sort(reverse=True)
# 计算标准差
price_std = np.std(data)
# 计算平均值
price_mean = np.mean(data)
# 对于一组给定的样本数据，其平均值为μ，标准偏差为σ，则其整体数据的平均值(1-α) 置信区间为 (μ-Ζα/2σ , μ+Ζα/2σ)，其中α为非置信水平在正态分布内的覆盖面积 ，Ζα/2 即为对应的标准分数
# 置信水平1-α	对应标准分数Zα/2
#    95%	1.96
#    90%	1.65
#    80%	1.28
price_range = [price_mean - price_std * 1.96, price_mean + price_std * 1.96]
a = 1
