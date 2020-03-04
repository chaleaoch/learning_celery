# -*- coding: UTF-8 -*-

from celery import Celery

app = Celery('tasks', backend='redis://192.168.31.254:6379', broker='amqp://guest@192.168.31.254:5672//')

app.conf.task_serializer = 'json'

app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Europe/Oslo',
    enable_utc=True,
)

app.config_from_object('celeryconfig')


@app.task
def add(x, y):
    return x + y
