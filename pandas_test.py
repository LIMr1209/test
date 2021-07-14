
# 中文文档
# https://www.pypandas.cn/docs/
import pandas as pd
import numpy as np

# 生成数据
s = pd.Series([1, 3, 5, np.NAN, 56], index=list('abcde'))

data = pd.date_range('20100101', periods=5, freq='Y')
t = s.copy()
t.index = data

df = pd.DataFrame(np.random.randn(5, 4), index=data, columns=list('ABCD'))
# print(df)

df2 = pd.DataFrame(
    {'A': 1.,
     'B': pd.Timestamp('20130102'),
     'C': pd.Series(1, index=list(range(4)), dtype='float32'),
     'D': np.array([3] * 4, dtype='int32'),
     'E': pd.Categorical(["test", "train", "test", "train"]),
     'F': 'foo'
     }
)

# 查看数据
# print(df.dtypes)
# print(df.head(1)) # 头
# print(df.tail(3)) # 尾
# print(df.index) # 索引
# print(df.columns) # 列
# print(df2.to_numpy()) # 转换
# print(df.describe()) # 统计
# print(df.T) # 转置
# print(df)
# print(df.sort_index(axis=0, ascending=False)) # 0 索引名 排序 1 列名排序
# print(df.sort_values(by='B', ascending=False)) # 值排序

# 选择
# print(df.A)
# print(df['A'])
# print(df[1:4])
# print(df['2011-12-31':'2012-12-31'])
# print(df.loc[data[1]])
# print(df.loc[data[1],['A','C']])
# print(df.loc[data[2]:,['A','C']])
# print(df.loc[data[0],['A']])
# print(df.at[data[0], 'A'])
# print(df.iloc[3])
# print(df.iloc[1:3, 0:2])
# print(df.iloc[[1, 2, 4], [0, 2]])
# print(df.iloc[1:3, :])
# print(df.iloc[1:3])
# print(df.iloc[:, 1:3])
# print(df.iloc[1, 1])
# print(df.iat[1,1])
# print(df[df.B > 0])
# print(df[df > 0])

# 赋值

df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four']
print(df2[df2['E'].isin(['two', 'four'])])

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20101231', periods=6, freq='Y'))
print(s1)

df['F'] = s1
print(df)

df.at[data[0], 'A'] = 0
df.iat[0, 1] = 0

df.loc[:, 'D'] = np.array([5] * len(df))

print(df)

df2 = df.copy()
df2[df2 > 0] = -df2
print(df2)

# 重建索引
df1 = df.reindex(index=data[0:4], columns=list(df.columns) + ['E'])
print(df1)

# 缺失值
# print(df1.dropna(how='any')) # 删除所有含缺失值的行：
# print(df1.fillna(value=5)) # 填充缺失值
# print(pd.isna(df1)) # 提取 nan 值的布尔掩码
# 运算
# print(df.mean()) # 列计算平均值
# print(df.mean(1)) # 行计算平均值

# s = pd.Series([1, 3, 5, np.nan, 6], index=data).shift(-1)
# print(s)
# print(df)
# print(df.sub(s, axis=1))
#
# print(df.apply(np.cumsum)) # np.cumsum 按行 累加 apply 执行函数
#
#
# print(df.apply(lambda x: x.max() - x.min()))
print(df.A.value_counts())
s = pd.Series(np.random.randint(0, 7, size=10))
print(s)
print(s.value_counts())

s = pd.Series(['A', 'B', np.NAN, 'CAB', 'a', 1])
print(s.str.lower())

# 合并
df = pd.DataFrame(np.random.randn(10, 4))

print(df)
pieces = [df[:3], df[3:7], df[7:]]
print(pd.concat(pieces))

# 连接
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})

right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})

print(pd.merge(left, right, on='key'))

left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})

right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})

print(pd.merge(left, right, on='key'))

# 追加

df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])

s = df.iloc[3]

print(df.append(s, ignore_index=True))  # 忽略 index

# 分组
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})
a = df.groupby('A').sum()
print(a.columns)
print(a.index)
b = df.groupby(['A', 'B']).sum()
print(b.index)

# 多层索引 堆叠
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]))

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8,2), index=index, columns=['A','B'])

df2 = df[:4]

print(df2)
a = df2.stack()
print(a)
print(a.index)

b = a.unstack()
print(b.index)
print(b.columns)
print(a.unstack(1))
print(a.unstack(0))

# 数据透视
df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                   'B': ['A', 'B', 'C'] * 4,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D': np.random.randn(12),
                   'E': np.random.randn(12)})
print(df)

print(pd.pivot_table(df, index=['A','B'], columns=['C'], values=['D', 'E']))

print(df.mean(0))
print(df.mean(1))
print(df.sum(0, skipna=False))
print(df.sum(1, skipna=True))

print(df.E.idxmin(), df.D.idxmax())  # 最小最大值对应的索引

