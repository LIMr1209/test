import pandas as pd
from matplotlib import pyplot as plt

# https://github.com/sripathikrishnan/redis-rdb-tools

sd = pd.read_csv('memory.csv')
sd.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
print(sd['size_in_bytes'].max())
data = sd.groupby(by=['database'])['size_in_bytes'].sum()
print(data)
print(sd['size_in_bytes'].sum())
