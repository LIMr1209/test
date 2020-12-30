from bson import ObjectId
from mongoengine import connect, Document, ListField, StringField, ObjectIdField, IntField, DictField

connect('test')


class User(Document):
    _id = ObjectIdField()
    tags = ListField(IntField())
    name = StringField()
    target_id = StringField()


# user = User()
# user.tags = [1, 2, 3]
# user.target_id = "test1"
# user.name = "张三"
# user.save()
#
# user = User()
# user.tags = [3, 5, 6]
# user.target_id = "test1"
# user.name = "李四"
# user.save()
#
# user = User()
# user.tags = [2, 5, 3]
# user.target_id = "test2"
# user.name = "王五"
# user.save()
#
# user = User()
# user.tags = [1, 5, 8]
# user.target_id = "test2"
# user.name = "赵二"
# user.save()
#
# user = User()
# user.tags = [1, 3, 4]
# user.target_id = "test3"
# user.name = "赵四"
# user.save()

# users = User._get_collection().find({"tags": {"$in": [ 5, 6 ]}})
# for i in users:
#     print(i["tags"])
# pipeline = [
#     # {"$match": {"tags": {"$in": [5, 6]}}},
#     {"$group": {"_id": "$target_id", "count": {"$sum": 1}, "img_id": {"$first": "$_id"}}},
#     {"$group":{"_id":"null","count":{"$sum":1}}}
# ]
#
# users_group = User.objects.aggregate(*pipeline)
# print(users_group)
# for i in users_group:
#     print(i)v
from pymongo.collation import Collation
#
# user = User._get_collection().find().sort("name", 1).collation(Collation(locale='zh'))
# for i in user:
#     print(i)
#
# user = User.objects.all()
# for i in user:
#     i.tags = [5,6,7]
#     i.save()

# import pymongo
#
# client = pymongo.MongoClient("127.0.0.1", authSource="admin")
# db = client["test"]
# product_collection = db["user"]
# doc = {"name":'佳栋', "tags": ['傻逼'], "target_id": '哈哈'}
# doc_two = {"name":'你妹', "tags": ['傻逼'], "target_id": '哈哈'}
#
# with client.start_session() as s:
#     s.start_transaction()
#     try:
#         product_collection.insert_one(doc, session=s)
#         product_collection.insert_one(doc_two, session=s)
#         a = '哈哈'
#         int(a)
#         s.commit_transaction()
#     except Exception as e:
#         s.abort_transaction()


class User(Document):
    _id = ObjectIdField()
    tags_test = ListField(default=[])
    name = StringField(default="")
    tags = ListField(IntField())
    target_id = StringField()
    a = IntField(default=0)

a = User.objects(tags__in=[7]).all()
for i in a:
    print(i.tags)
# a = User()
# a.tags = [13,2]
# a.save()
# a.reload()
# print(a._id)