#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by null 2018-04-28 15:56:12

from default import Config

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@ip:port/db?charset=charcode'
    SQLALCHEMY_ECHO = False
    
    # -----------------------------
    # Redis server configure
    # -----------------------------
    REDIS_HOST = 'xx.xx.xxx.xxx'
    REDIS_PORT = xxx
    REDIS_PASSWORD = ''
    REDIS_DB = 0
    REDIS_TIMEOUT = 30

