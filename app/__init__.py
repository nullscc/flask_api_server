#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by null 2018-04-28 15:45:49

from flask import Flask, request, abort, current_app, Response
from werkzeug.datastructures import Headers
from app.config import load_config
from app import views
import json
from app.lib.db import RedisApi, db
from app.services.base_service import BaseService
import uuid

DEFAULT_MODULES = (
    (views.index, ''),
    (views.user, '/user'),
)

WHITE_PATH = [
    "/login",
    "/user/login"
]

def check_token(token):
    return current_app.simple_cache.get(token)
    
def hook_init(app):
    @app.before_request
    def token_check():
        if request.path in WHITE_PATH:
            return
        token = request.headers.get("token", "")
        if not token or not check_token(token):
            return abort(403)

def hook_error_handler(app):
    @app.errorhandler(403)
    def forbidden(error):
        return BaseService.render_json(data=None, code=403, msg="Please login")

class MyResponse(Response):
    def __init__(self, response=None, **kwargs):
        kwargs['headers'] = ''
        headers = kwargs.get('headers')
        # 跨域控制 
        origin = ('Access-Control-Allow-Origin', '*')
        methods = ('Access-Control-Allow-Methods', '*')
        content_type = ("Access-Control-Allow-Headers", "Content-Type,Access-Token,token")
        if headers:
            headers.add(*origin)
            headers.add(*methods)
        else:
            headers = Headers([origin, methods, content_type])
        kwargs['headers'] = headers
        return super().__init__(response, **kwargs)

def create_app():
    app = Flask(__name__)
    app.config.from_object(load_config())
    db.init_app(app)

    for module, url_prefix in DEFAULT_MODULES:
        app.register_blueprint(module, url_prefix=url_prefix)
    app.simple_cache = RedisApi(host=app.config['REDIS_HOST'],
            port=app.config['REDIS_PORT'],
            password=app.config['REDIS_PASSWORD'],
            db=app.config['REDIS_DB'])
    hook_init(app)
    hook_error_handler(app)
    app.response_class = MyResponse
    return app
