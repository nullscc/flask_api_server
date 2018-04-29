import json
import types
from decimal import Decimal
import datetime
from sqlalchemy.util import KeyedTuple
from flask_sqlalchemy import Model 
import time

def to_json(ret=0, msg='ok', data=None):
    now = int(time.time())
    jsondata = {'code':ret, 'msg':msg, 'timestamp':now}

    if not data:
        return json.dumps(jsondata)

    jsondata['info'] = data
    return json_encode(jsondata)

def json_encode(data):

    def _any(data):
        ret = None
        if isinstance(data, list):
            ret = _list(data)
        elif isinstance(data, dict):
            ret = _dict(data)
        elif isinstance(data, Decimal):
            ret = str(data)
        elif isinstance(data, Model):
            ret = _model(data)
        elif isinstance(data, KeyedTuple):
            ret = _dict(data._asdict())
        elif isinstance(data, datetime.datetime):
            ret = _datetime(data)
        elif isinstance(data, datetime.date):
            ret = _date(data)
        elif isinstance(data, datetime.time):
            ret = _time(data)
        else:
            ret = data

        return ret

    def _model(data):
        ret = {}
        for c in data.__table__.columns:
            ret[c.name] = _any(getattr(data, c.name))

        return ret

    def _list(data):
        ret = []
        for v in data:
            ret.append(_any(v))
        return ret

    def _dict(data): 
        ret = {}
        for k,v in data.items():
            ret[k] = _any(v)
        return ret

    def _datetime(data):
        return data.strftime("%s %s" % ("%Y-%m-%d", "%H:%M:%S"))

    def _date(data):
        return data.strftime("%Y-%m-%d")

    def _time(data):
        return data.strftime("%H:%M:%S")

    ret = _any(data)

    return json.dumps(ret)

