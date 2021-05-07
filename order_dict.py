import json
from collections import OrderedDict  # 有序字典

foo = {'b': 1, 'c': 2}

# 无序字典转为有序字典
foo = OrderedDict(foo)
# foo == OrderedDict([('c', 2), ('b', 1)])

foo['a'] = 0
# foo == OrderedDict([('c', 2), ('b', 1), ('a', 0)])
a = foo.pop(0)
print(a)
print(foo)
# 简单有序字典转为无序字典
foo = dict(foo)
# foo == {u'a': 0, u'c': 2, u'b': 1}

# 复杂有序字典转为无序字典
bar = OrderedDict({'a': OrderedDict(b=0, c=1)})
print(bar)
# bar == OrderedDict([('a', OrderedDict([('c', 1), ('b', 0)]))])
bar = json.loads(json.dumps(bar))
print(bar)
