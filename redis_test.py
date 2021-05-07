# -*- coding: utf-8 -*-
#
# Redis database operation method
import redis


class RedisHandle(object):

    def __init__(self, host, port, password=None):
        self.conn = redis.Redis(host, port, password)

    def insert(self, name, key, value):
        self.conn.hset(name, key, value)

    def query(self, name, key):
        rst = self.conn.hget(name, key)
        return rst

    def verify(self, name, key):
        rst = self.conn.hexists(name, key)
        return rst


if __name__ == '__main__':
    RH = RedisHandle('localhost', '6379')
    RH.insert('jd','page',2)
    RH.insert('jd', 'keyword', "水壶")
    print(int(RH.query('jd', 'page')))
    print(RH.verify('jd','page'))