# -*- coding: UTF-8 -*-

from celery import Celery

app = Celery('tasks', backend='redis://192.168.31.254:6379', broker='amqp://guest@192.168.31.254:5672//')


@app.task
def add(x, y):
    return x + y
