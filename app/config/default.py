#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by null 2018-04-28 16:03:37

class Config(object):
    # mysql config
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_POOL_RECYCLE = 280
    SQLALCHEMY_POOL_TIMEOUT = 1800
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@123456@127.0.0.1/test?charset=utf8'
    SQLALCHEMY_ECHO = False
    
    # -----------------------------
    # Redis server configure
    # -----------------------------
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    
    REDIS_PASSWORD = ''
    REDIS_DB = 0
    REDIS_TIMEOUT = 30

