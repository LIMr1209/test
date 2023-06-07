import pymongo


class Connection:
    def __init__(self, collect_name):
        self.collection = pymongo.MongoClient(
            host="127.0.0.1",
            username="facemodelapi",
            password="123456",
            # 由于PyMongo不是进程安全的, 禁止MongoClient实例在进程之间的传递
            connect=False,  # `connect`（可选）：如果`True`（默认值），立即开始在后台连接MongoDB。否则，在第一次操作时进行连接。
            authSource="facemodelapi",
            serverSelectionTimeoutMS=5000  # 连接超时5秒
        )["facemodelapi"][collect_name]

    def insert(self, item):
        """
        插入数据
        :param item: dict
        :return: 插入返回的ObjectId
        """
        return self.collection.insert_one(item).inserted_id

    def update(self, condition, update_dict):
        """
        更新數據
        :param condition: 条件
        :param update_dict: 更新的数据
        :return:
        """
        return self.collection.update_many(condition, {'$set': update_dict})

    def delete(self, condition):
        """
        刪除數據
        :param condition: 条件
        :return:
        """
        return self.collection.delete_many(condition)

    def count(self, condition):
        """
        查询数量
        :param condition: 条件
        :return:
        """
        return self.collection.count_documents(condition)

    def fetchone_to_dict(self, condition, projection={}, sort=[]):
        """
        查询单条
        :param projection:  {'_id':0,'timestamp':0} 使用0或1，来表示不显示或显示指定字段  除’_id’以外，不能在一个对象中同时指定 0 和 1，如果你设置了一个字段为 0，则其他都为 1，反之亦然。
        :param condition: 条件
        :param sort: [('name', 1), ("_id", -1)]
        :return:
        """
        return self.collection.find_one(condition, projection=projection, sort=sort)

    def fetch_to_page(self, condition, page_num, page_size, projection={}, sort=[]):
        """
        分页查询
        :param projection: 字段显示或者隐藏
        :param condition: 条件
        :param page_num: 页数
        :param page_size: 大小
        :param sort: [('name', -1), ("_id", -1)]
        :return:
        """
        items_skipped = (page_num - 1) * page_size
        cursor = self.collection.find(condition, projection=projection).skip(items_skipped)
        if len(sort) > 0:
            cursor = cursor.sort(sort).limit(page_size)
        else:
            cursor = cursor.limit(page_size)

        items = [i for i in cursor]
        return items

    def fetchall_to_list(self, condition, projection={}, sort=[]):
        """
        查询多条
        :param projection: 字段显示或者隐藏
        :param condition:  条件
        :param sort: [('name', 1), ("_id", -1)]
        :return:
        """
        cursor = self.collection.find(condition, projection=projection, sort=sort)
        items = [i for i in cursor]
        return items

    def fetch_aggregate(self, pipeline):
        """
        聚合查询
        :param pipeline: 聚合条件
        :return:
        """
        cursor = self.collection.aggregate(pipeline)
        items = [i for i in cursor]
        return items
