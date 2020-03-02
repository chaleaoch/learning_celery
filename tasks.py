# -*- coding: UTF-8 -*-

from celery import Celery

app = Celery('tasks', broker='amqp://guest@192.168.31.254:5672//')


# app = Celery('tasks', backend='rpc://', broker='amqp://guest@192.168.31.254:5672//')


@app.task
def add(x, y):
    return x + y
