#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by null 2018-04-29 10:36:13

from app.services.base_service import BaseService
from flask import request
from app.models.admin import Admin
from hashlib import md5
from uuid import uuid1

class UserService(BaseService):
    
    @staticmethod
    def gen_token():
        return str(uuid1())
        
    def login(self):
        def err_handler(msg=None):
            self.code = 1
            if not msg:
                self.msg = "用户名或密码错误"
            else:
                self.msg = msg
        username = request.form.get("username", "") 
        password = request.form.get("password", "") 
        if not username or not password:
            err_handler()
            return
        admin = Admin.query.filter(Admin.admin_name == username).first()
        if not admin:
            err_handler()
            return

        passwd_error_time_cache = 'PASSWD_ERROR_{}'.format(username)
        error_time = self.redis_db.get(passwd_error_time_cache)
        if error_time and int(error_time) >= 5:
            msg = "密码错误次数太多，已被锁定请稍后再试!"
            err_handler(msg)
            return

        md5_pwd = md5(password.encode("utf-8")).hexdigest()
        if admin.admin_pwd != md5_pwd:
            self.redis_db.incr(passwd_error_time_cache)
            if error_time:
                self.redis_db.expire(passwd_error_time_cache, 15*60)
            err_handler()
            return

        self.redis_db.delete(passwd_error_time_cache)
        this_token = self.gen_token()
        self.redis_db.set_bylock(this_token, admin.id, 30*24*3600)
        self.data = {"token":this_token}

    def get_info(self):
        name = self.session.query(Admin.admin_name).filter(Admin.id==self.uid).scalar()
        avatar = "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif"
        self.data = {"name":name, "avatar": avatar}

    def logout(self): 
        self.redis_db.delete(request.headers.get("token", ""))
        
