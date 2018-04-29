#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by null 2018-04-28 16:48:10

from flask import current_app, request
from app.lib.common import to_json
from app.lib.db import db
from werkzeug.datastructures import Headers

class BaseService(object):
    def __init__(self):
        self.code = 0
        self.msg = "ok"
        self.data=None
        self.session = db.session
        self.redis_db = current_app.simple_cache
        self.uid = 0
        token = request.headers.get("token")
        if token:
            self.uid = int(self.redis_db.get_bylock(token) or 0)
    
    @staticmethod
    def render_json(data=None, code=0, msg="ok"):
        res = current_app.response_class(mimetype='application/json')
        res.data = to_json(code, msg, data)
        return res

    def render(self):
        return self.render_json(self.data, self.code, self.msg)
                

