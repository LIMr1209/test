import itertools

# 1. 组合生成器

# 组合可迭代对象
for item in itertools.product([1,2,3,4], [5,6,7,8]):
    print(item)

# 对可迭代对象的元素生成不同的排列组合 组合的个元素顺序不同
print(list(itertools.permutations([1,2,3,4])))

# 对可迭代对象的元素生成不同的排列组合 组合的个元素顺序不同(指定长度)
print(list(itertools.permutations([1,2,3,4],2)))

# 对可迭代对象的元素生成不同的排列组合 不考虑元素顺序(指定长度)
print(list(itertools.combinations([1,2,3,4], 2)))

# 2.无限迭代器

# 作用: 返回以start开头的均匀间隔step步长的值
for item in itertools.count(10,3):
    if item>100:
        break
    print(item)


# 作用:保存迭代对象的每个元素的副本，无限的重复返回每个元素的副本
its=["a","b","c","d"]
# for item in itertools.cycle(its):
#     print(item)

# 按照指定的迭代次数重复返回每次的迭代对象
for item in itertools.repeat(its,4):
    print(item)


# 3.有限迭代器

# 作用:返回所有可迭代序列
its=["a","b","c","d"]
hers=["A","B","C","D"]
others=["1","2","3","4"]
for item in itertools.chain(its,hers,others):
    print(item)


# 返回数据对象中对应规则为True的元素
its=["a","b","c","d","e","f","g","h"]
selector=[True,False,1,0,3,False,-2,"y"]
for item in itertools.compress(its,selector):
    print(item)


print(list(range(5)))
