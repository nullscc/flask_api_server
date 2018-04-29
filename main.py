#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by null 2018-04-28 15:32:06

import os
from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True, port=9888)
