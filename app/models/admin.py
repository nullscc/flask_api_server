#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by null 2018-04-29 10:45:35
from app.lib.db import db

class Admin(db.Model):
    __tablename__ = 'fanwe_admin'

    id = db.Column(db.Integer, primary_key=True)
    admin_name = db.Column(db.String(60), default='')
    admin_pwd = db.Column(db.String(32), default='')
    last_login_time = db.Column(db.Integer, default=0)
    last_login_ip = db.Column(db.String(40), default=None)
    login_count = db.Column(db.Integer, default=0)
    create_time = db.Column(db.Integer, default=0)
    update_time = db.Column(db.Integer, default=0)
    status = db.Column(db.Integer, default=0)
    role_id = db.Column(db.Integer, default=0)
    timezone = db.Column(db.String(32), default='Asia/Shanghai')
    email = db.Column(db.String(64), default='')

    def __str__(self):
        return "Admin => { \
id:%d, admin_name:'%s', admin_pwd:'%s', last_login_time:%d, last_login_ip:'%s',  \
login_count:%d, create_time:%d, update_time:%d, status:%d, role_id:%d, \
timezone:'%s', email:'%s'}" % (
            self.id, self.admin_name, self.admin_pwd, self.last_login_time, self.last_login_ip,
            self.login_count, self.create_time, self.update_time, self.status, self.role_id,
            self.timezone, self.email)

    __repr__ = __str__



