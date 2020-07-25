# -*- coding: UTF-8 -*-

from __future__ import absolute_import, unicode_literals
from .celery import app
from time import sleep
from datetime import datetime, timezone

@app.task
def add(x, y):
    print(datetime.now())
    print(1233333333333333)
    # sleep(100)
    return x + y

@app.task
def mul(x, y):
    return x * y

@app.task
def xsum(numbers):
    return sum(numbers)