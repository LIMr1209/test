import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
# print(x)
# print(x.ndim) # 维数
# print(x.size) # 大小
# print(x.real) # 实部
# print(x.imag) # 虚部
# for i in x.flat: # 迭代器
#     print(i)
# print(x.T) # 转置
# print(x.shape) # 维度元组
# print(x.dtype) # 类型
# print(x[1, 2]) # 取值
# print(x[:,:2])


# 广播
arr1 = np.random.randn(3,4,5)
print(arr1)
arr2 = arr1.mean(axis=1)[:,np.newaxis,:]
print(arr2)
arr3 = arr1-arr2
print(np.around(arr3.mean(0),2))
