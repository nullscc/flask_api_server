#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by null 2018-04-28 16:11:35

from flask import Blueprint
import json
from app.services.base_service import BaseService

index = Blueprint('index', __name__)

@index.route('/test')
def test():
    return BaseService().render()


