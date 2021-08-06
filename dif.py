a = [{"id":1, "year": 2020},{"id":2, "year": 2020},{"id":3, "year": 2020},{"id":4, "year": 2020}]
b = [{"id":4, "year": 2020},{"id":5, "year": 2020},{"id":6, "year": 2020},{"id":7, "year": 2020}]

# difference() 方法用于返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中。
old_prize_id = set.difference(*[{d['id'] for d in ls} for ls in [a, b]])
new_prize_id = set.difference(*[{d['id'] for d in ls} for ls in [b, a]])
print(list(old_prize_id))
print(new_prize_id)
for i in new_prize_id:
    print(i)

