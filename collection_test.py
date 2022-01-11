import json
from collections import OrderedDict, Counter, deque, defaultdict, namedtuple

# 有序字典 OrderedDict
# 排序的字段。父类为Python内置的dict

foo = {'b': 1, 'c': 2}

# 无序字典转为有序字典
foo = OrderedDict(foo)
# foo == OrderedDict([('c', 2), ('b', 1)])

foo['a'] = 0
# foo == OrderedDict([('c', 2), ('b', 1), ('a', 0)])
a = foo.pop('a')
print(a)
print(foo)
# 简单有序字典转为无序字典
foo = dict(foo)
# foo == {u'a': 0, u'c': 2, u'b': 1}
print(foo)

# 复杂有序字典转为无序字典
bar = OrderedDict({'a': OrderedDict(b=0, c=1)})
print(bar)
# bar == OrderedDict([('a', OrderedDict([('c', 1), ('b', 0)]))])
bar = json.loads(json.dumps(bar))
print(bar)

# 计数器 Counter
# 统计可哈希的对象。父类为Python内置的dict

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)

# 出现频率最高的三个单词
top_three = word_counts.most_common(3)
print(top_three)
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]
print(word_counts['eyes'])

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']

# 如果你想手动增加计数，可以简单的用加法：
for word in morewords:
    word_counts[word] += 1
print(word_counts['eyes'])

# 双端队列 deque 用途：双端队列，头部和尾部都能以O(1)时间复杂度插入和删除元素。类似于列表的容器
# 头部插入与删除的时间复杂度为O(1)，
d = deque()
d.append(1)
d.append("2")
print(len(d))
print(d[0], d[1])
d.extendleft([0])
print(d)
d.extend([6, 7, 8])
print(d)

d2 = deque('12345')
print(len(d2))
d2.popleft()
print(d2)
d2.pop()
print(d2)

# 在队列两端插入或删除元素时间复杂度都是 O(1) ，区别于列表，在列表的开头插入或删除元素的时间复杂度为 O(N)
d3 = deque(maxlen=2)
d3.append(1)
d3.append(2)
print(d3)
d3.append(3)
print(d3)

# defaultdict  带有默认值的字典。父类为Python内置的dict
# defaultdict  的一个特征是它会自动初始化每个 key 刚开始对应的值，所以你只需要 关注添加元素操作了。比如：

d = defaultdict(list)
print(d)
d['a'].append([1, 2, 3])
d['b'].append(2)
d['c'].append(3)

print(d)

d = defaultdict(set)
print(d)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

print(d)

# namedtuple()  用途：创建命名字段的元组。工厂函数
# namedtuple主要用来产生可以使用名称来访问元素的数据对象，通常用来增强代码的可读性， 在访问一些tuple类型的数据时尤其好用。

websites = [
    ('Sohu', 'http://www.sohu.com/', u'张朝阳'),
    ('Sina', 'http://www.sina.com.cn/', u'王志东'),
    ('163', 'http://www.163.com/', u'丁磊')
]

Website = namedtuple('Website', ['name', 'url', 'founder'])

for website in websites:
    website = Website._make(website)
    print(website)
    print(website.url)
    print(website.name)
    print(website.founder)

# ChainMap 创建多个可迭代对象的集合。类字典类型

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
# 现在假设你必须在两个字典中执行查找操作
# (比如先从 a 中找，如果找不到再在 b 中找)。
# 一个非常简单的解决方案就是使用collections模块中的ChainMap类
from collections import ChainMap

c = ChainMap(a, b)

print(c)

a['x'] = 11  # 使用ChainMap时，原字典做了更新，这种更新会合并到新的字典中去

print(c)  # 按顺序合并两个字典
print(c['x'])
print(c['y'])
print(c['z'])  # 按顺序获取字典元素

# 对于字典的更新或删除操作影响的总是列中的第一个字典。
c['z'] = 10
c['w'] = 40
del c['x']
print(a)
print(c)
# del c['y']将出现报错


values = ChainMap()  # 默认会创建一个空字典
print('\t', values)
values['x'] = 1
values = values.new_child()  # 添加一个空字典
values['x'] = 2
values = values.new_child()
values['x'] = 30
print(values)
print(values, values['x'])  # values['x']输出最后一次添加的值
values = values.parents  # 删除上一次添加的字典
print(values)
print(values['x'])
values = values.parents
print(values)
