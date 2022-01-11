# import pymongo
# client = pymongo.MongoClient("127.0.0.1", authSource="admin")
# db = client["test"]
# product_collection = db["user"]
# doc = {"name":'佳栋', "tags": ['傻逼'], "target_id": '哈哈'}
# doc_two = {"name":'你妹', "tags": ['傻逼'], "target_id": '哈哈'}
#
# # 事务
# with client.start_session() as s:
#     s.start_transaction()
#     try:
#         product_collection.insert_one(doc, session=s)
#         product_collection.insert_one(doc_two, session=s)
#         a = '哈哈'
#         int(a)
#         s.commit_transaction()
#     except Exception as e:
#         print('11')
#         s.abort_transaction()


from mongoengine import connect, Document, ListField, StringField, ObjectIdField, IntField, ReferenceField
from mongoengine.queryset.visitor import Q
import json

connect('test')


# class Card(Document):
#     meta = {
#         "id_field": "_id",
#         'strict': True,
#     }
#     id = ObjectIdField()
#     number = StringField()


class User(Document):
    meta = {
        "id_field": "_id",
        'strict': True,
        'indexes': ['+name'],  # 索引名
        'auto_create_index': False,  # 禁止自动创建索引
    }
    _id = ObjectIdField()
    tags_test = ListField(default=[])
    name = StringField(default="")
    tags = ListField(IntField())
    target_id = StringField()
    a = IntField(default=0)
    b = IntField(default=0)
    # c = ReferenceField(Card)


# User.create_index('name',True) # 创建索引  不推荐
# User.drop_collection() # 删除数据库集合
# a = User.compare_indexes() # 将MongoEngine中定义的索引与数据库中现有的索引进行比较。返回所有丢失/额外的索引。
# User.ensure_index('-name', True) # 创建索引
# a = User.from_json(json.dumps({"name":'佳栋', "tags": ['傻逼'], "target_id": '哈哈'})) # json 转 doc
# print(a.pk) # 主键
# a = User.list_indexes() # 列出应为给定集合创建的所有索引。它包括超类和子类的所有索引。

# a = User.objects(name='bbbbb').where("this.a+1 > this.b+1").all() # 谓语过滤
# a = User.objects.item_frequencies('name') # 返回整个查询的文档集中某个字段中存在的所有项目的字典，以及它们的相应频率

# a = User.objects.first()
# a.switch_collection('test') # 临时切换集合
# a.switch_db('archive-db') # 临时切换数据库
# a.save()
# a = User.objects(name="张三")
# a.to_json() # 转换位json
# a.to_mongo() # 转换mongo
# a.to_dict() # 转换字典
# a.validate() # 验证字段

# a = User.objects(name="张三").__call__(target_id="test2").count() # __call__ 查询结果，过滤
# print(User.objects.average('a')) # a字段 平均值

# print(User.objects(name="张三").explain()) # 查询计划
# print(User.objects(name="张三").hint('name_1')) # 指定使用索引查询
#
# aggregate = [
#     {
#         '$match':
#             {
#                 'name': '张三'
#             },
#     },
#     {
#     '$addFields': {
#            'count': { "$sum": ["$a","$b"]}
#          }
#     },
#     {"$sort":
#          {"count": 1}
#     }
# ]
# a = User._get_collection().aggregate(aggregate)
# for i in a:
#     print(i)


query = {'tags__0': 6}

user = User.objects(**query).all()
for i in user:
    print(i.to_mongo())
