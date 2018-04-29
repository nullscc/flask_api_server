#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by null 2018-04-28 15:53:11

import os

def load_config():
    """加载配置类"""
    mode = os.getenv('ADMIN_ENV', '.dev')
    if mode != '.dev':
        from .production import ProductionConfig
        return ProductionConfig
    else:
        from .dev import DevelopmentConfig
        return DevelopmentConfig
    return Config
