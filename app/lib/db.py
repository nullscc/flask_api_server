#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by null 2018-04-29 11:04:26

import redis
from flask_sqlalchemy import SQLAlchemy
import time, math, json

db = SQLAlchemy()

class RedisApi(redis.Redis):

    def get_json(self, name):
        """
        如果和老的api设置的值可以用这个方法取
        :param name:
        :return:
        """
        value = self.get(name)
        if value is None:
            return None
        try:
            return json.loads(value)
        except Exception:
            if value.startswith(b'!'):
                try:
                    return json.loads(pickle.loads(value[1:]))
                except pickle.PickleError:
                    return None
            else:
                return json.loads(value.decode().replace("'", '"'))

    def get_bylock(self, key):
        """
        避免redis超时时的惊群现象，请必须配合 `set_bylock` 使用

        调用方法与`get`一样
        """
        lock_key = key + ".lock"

        data = self.get(key)
        current = int(time.time())
        if not data:
            return None
        else:
            real_data = json.loads(data)
            # 如果人为设置的超时时间超时了
            if real_data['expireat'] <= current:
                # 如果获取到锁
                if self.set(lock_key, "x", ex=2, nx=True):
                    return None
                # 如果没获取到锁
                else:
                    return real_data['data']
            else:
                return real_data['data']

    def set_bylock(self, key, data, expire_time):
        """
        避免redis超时时的惊群现象，请必须配合`get_bylock`使用

        调用方法与`setex`一样
        """
        current = int(time.time())
        real_data = {'data': data, 'expireat': current + expire_time - math.ceil(expire_time / 2)}
        self.setex(key, json.dumps(real_data), expire_time)

