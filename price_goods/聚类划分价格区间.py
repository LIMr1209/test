import pandas as pd
from matplotlib import pyplot as plt
from interval import Interval
import os
import numpy

# https://blog.csdn.net/weixin_34277853/article/details/94607777
tag = '电动牙刷'
if not os.path.exists('result/{}'.format(tag)):
    os.makedirs('result/{}'.format(tag))
sd = pd.read_csv('{}.csv'.format(tag))
# sd = pd.read_table()
sd.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
# 画散点图（横轴：价格，纵轴：销量）#设置图框大小
fig = plt.figure(figsize=(10, 6))
plt.plot(sd['price'], sd['sale_count'], "o")
# 展示x，y轴标签
plt.xlabel('price')
plt.ylabel('sale_count')
plt.savefig('result/{}/origin.jpg'.format(tag))
plt.show()

fig = plt.figure(figsize=(10, 6))
# 初始化两个子图，分布为一行两列
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
# 绘制箱型图
ax1.boxplot(sd['price'].values)
ax1.set_xlabel('price')
ax2.boxplot(sd['sale_count'].values)
ax2.set_xlabel('sale_count')
# 设置x，y轴取值范围
ax1.set_ylim(0, sd['price'].max())
ax2.set_ylim(0, sd['sale_count'].max())
# plt.show()

abnormal_price = 1000
abnormal_sale_count = 12000
price_range_len = 4
# 删除价格￥120以上，评论数700以上的数据
data2 = sd[sd['price'] < abnormal_price]
data3 = data2[data2['sale_count'] < abnormal_sale_count]
# data3为异常值处理后的数据
fig = plt.figure(figsize=(10, 6))
plt.plot(data3['price'], data3['sale_count'], "o")
plt.xlabel('price')
plt.ylabel('sale_count')
plt.savefig('result/{}/filter.jpg'.format(tag))
plt.show()

price_range = []
for i in range(price_range_len):
    if i == 0:
        price_range.append([0, int(abnormal_price / price_range_len)])
    elif i == price_range_len - 1:
        price_range.append([int(abnormal_price / price_range_len * i) + 1])
    else:
        price_range.append(
            [int(abnormal_price / price_range_len * i) + 1, int(abnormal_price / price_range_len * (i + 1))])

zoom_1 = Interval(*price_range[0])
zoom_2 = Interval(*price_range[1])
zoom_3 = Interval(*price_range[2])
data = []
for row in sd.itertuples():
    if getattr(row, 'price') in zoom_1:
        price_range_text = '{}-{}'.format(price_range[0][0], price_range[0][1])
    elif getattr(row, 'price') in zoom_2:
        price_range_text = '{}-{}'.format(price_range[1][0], price_range[1][1])
    elif getattr(row, 'price') in zoom_3:
        price_range_text = '{}-{}'.format(price_range[2][0], price_range[2][1])
    elif getattr(row, 'price') >= price_range[3][0]:
        price_range_text = '{}以上'.format(price_range[3][0])
    for i in data:
        if i['name'] == price_range_text:
            i['value'] += getattr(row, 'sale_count')
            break
    else:
        data.append({
            'name': price_range_text,
            'value': getattr(row, 'sale_count')
        })

from pyecharts.charts import Bar

bar = Bar()
x = [i['name'] for i in data]
y = [i['value'] for i in data]
bar.add_xaxis(x)
bar.add_yaxis('价格', y)
bar.render("result/{}/result.html".format(tag))
# # 求最值
# pricemax=data3['price'].max()
# pricemin=data3['price'].min()
# salemax=data3['sale_count'].max()
# salemin=data3['sale_count'].min()
# ##计算极差
# pricerg=pricemax-pricemin
# salerg=salemax-salemin
# #组距=极差/组数
# pricedst=pricerg/13
# salest=salerg/13
# fig = plt.figure(figsize=(12,5))
# ax1 = fig.add_subplot(1,2,1)
# ax2 = fig.add_subplot(1,2,2)
#
# # 绘制价格直方图#numpy.arrange(最小,最大,组距)
# pricesty=np.arange(pricemin,pricemax,pricedst)
# ax1.hist(data3['price'],pricesty,rwidth=0.8)
# ax1.set_title('price')
# #绘制评论数直方图
# commentsty=np.arange(salemin,salemax,salest)
# ax2.hist(data3['sale_count'],commentsty,rwidth=0.8)
# ax2.set_title('sale_count')
# plt.show()


#转换数据格式
# tmp=numpy.array([data3['price']]).T
# #调用python关于机器学习sklearn库中的KMeans
# from sklearn.cluster import KMeans
# #设置分为3类，并训练数据
# kms=KMeans(n_clusters=4)
# y=kms.fit_predict(tmp)
# #将分类结果以散点图形式展示
# fig = plt.figure(figsize=(10,6))
# plt.xlabel('price')
# # plt.ylabel('price')
# for i in range(0,len(y)):
#     if(y[i]==0):
#         plt.plot(tmp[i,0],"*r")
#     elif(y[i]==1):
#         plt.plot(tmp[i,0],"sy")
#     elif(y[i]==2):
#         plt.plot(tmp[i,0],"pb")
# plt.show()
