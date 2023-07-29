import time

from pymongo import MongoClient

url = "mongodb://facemodelapi:123456@10.25.10.132:27017, 10.25.10.22:27017/facemodelapi?replicaSet=rs0&authSource=facemodelapi&serverSelectionTimeoutMS=5000"
# url = "mongodb://facemodelapi:123456@10.25.20.15:27017/facemodelapi?authSource=facemodelapi&serverSelectionTimeoutMS=5000"

client = MongoClient(url)
client.read_preference = MongoClient.SECONDARY
print(client.is_mongos)
print(client.is_primary)
collection = client["facemodelapi"]["student"]

session = client.start_session(causal_consistency=True)

# 开启事务会话
# session.start_transaction(max_commit_time_ms=5000) # 超过5 秒 自动回滚
# 如果一个事务执行的时间超过了5秒钟，那么 MongoDB 将会回滚该事务并返回一个错误。这可以帮助开发人员保持对数据库资源的有效利用，并且在某些情况下，防止出现死锁或长时间运行的事务。
session.start_transaction()
collection.update_one({"world":100}, {"$set": {"world": 200}}, session=None)

try:
    collection.update_one({"world":100}, {"$set": {"world": 200}}, session=session)
    collection.delete_one({"world": 100}, session=session)
    # 正常插入数据
    collection.insert_one({'0': '正常插入数据'}, session=session)

    # 异常插入数据
    collection.insert_one({0: '异常插入数据'}, session=session)

    # 抛出一个错误
    # raise ValueError('抛出一个错误')

except Exception as e:

    # 操作异常 中断事务
    session.abort_transaction()

    # 输入异常内容
    print(e)

else:
    # 操作正常 提交事务
    session.commit_transaction()
finally:
    # 关闭事务会话
    session.end_session()


for i in collection.find():
    print(i)
