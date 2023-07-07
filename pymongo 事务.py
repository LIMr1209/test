from pymongo import MongoClient

url = "mongodb://facemodelapi:123456@lzb:27017/facemodelapi?replicaSet=rs0&authSource=facemodelapi&serverSelectionTimeoutMS=5000"

client = MongoClient(url)
collection = client["facemodelapi"]["student"]

session = client.start_session(causal_consistency=True)

# 开启事务会话
session.start_transaction()

try:
    collection.update_one({"world":100}, {"$set": {"world": 200}}, session=session)
    collection.delete_one({"world": 100}, session=session)
    # 正常插入数据
    collection.insert_one({'0': '正常插入数据5'}, session=session)

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

